import streamlit as st  
import requests  
import pandas as pd  
import plotly.express as px  
from datetime import datetime, timedelta  
import sys  
import io  


BODY_CODES = {  
    'Mercury': 'Merc',  
    'Venus': 'Venus',  
    'Earth': 'Earth',  
    'Mars': 'Mars',  
    'Jupiter': 'Juptr',  
    'Saturn': 'Satrn',  
    'Uranus': 'Urnus',  
    'Neptune': 'Neptn',  
    'Moon': 'Moon'  
    
}


def fetch_close_approaches(body_code='Earth', date_min='now', date_max='+60', dist_max='0.05', dist_unit='AU', limit=100, object_type='NEO'):  
    url = 'https://ssd-api.jpl.nasa.gov/cad.api'  
    params = {  
        'body': body_code,  
        'date-min': date_min,  
        'date-max': date_max,  
        'dist-max': f"{dist_max}{dist_unit}",  
        'limit': limit  
    }
    
    
    if object_type == 'NEO':  
        params['neo'] = 'true'  
    elif object_type == 'Comet':  
        params['comet'] = 'true'  
    
    try:  
        response = requests.get(url, params=params)  
        response.raise_for_status()  
        data = response.json()  
        return data  
    except requests.exceptions.HTTPError as http_err:  
        st.error(f"⚠️ HTTP error occurred: {http_err}")  
        try:  
            error_info = response.json()  
            st.error(f"🔍 Error details: {error_info}")  
        except ValueError:  
            st.error("🔍 No additional error information provided.")  
        return None  
    except requests.exceptions.RequestException as e:  
        st.error(f"⚠️ Error fetching data from API: {e}")  
        return None  


def parse_data(data):  
    if data is None or data.get('count', 0) == 0:  
        st.warning("⚠️ No close approaches found for the given parameters.")  
        return pd.DataFrame()  
    
    fields = data.get('fields', [])  
    records = data.get('data', [])  
    df = pd.DataFrame(records, columns=fields)  
    
    
    df['cd'] = pd.to_datetime(df['cd'], format='%Y-%b-%d %H:%M')  
    df['dist'] = pd.to_numeric(df['dist'], errors='coerce')  
    df['v_rel'] = pd.to_numeric(df['v_rel'], errors='coerce')  
    df['v_inf'] = pd.to_numeric(df['v_inf'], errors='coerce')  
    
    return df  


def visualize_close_approaches(df, body, add_trendline=False):  
    if df.empty:  
        return  
    
    
    if add_trendline:  
        try:  
            import statsmodels.api as Agnirvastatsmodels  
        except ImportError:  
            st.warning("⚠️ Statsmodels is not installed. Trendline feature is disabled.")  
            add_trendline = False  
    
    if add_trendline:  
        trendline = "ols"  
    else:  
        trendline = None  
    
    fig = px.scatter(  
        df,  
        x='cd',  
        y='dist',  
        hover_data=['des', 'v_rel', 'v_inf'],  
        labels={  
            'cd': '📅 Date',  
            'dist': f'📏 Distance ({st.session_state.get("dist_unit", "AU")})',  
            'des': '🪐 Designation',  
            'v_rel': '⚡ Relative Velocity (km/s)',  
            'v_inf': '∞ Infinity Velocity (km/s)'  
        },
        title=f'🔭 Close Approaches to {body}',  
        trendline=trendline  
    )
    
    fig.update_yaxes(autorange="reversed")  
    st.plotly_chart(fig, use_container_width=True)  


def main():  
    st.set_page_config(page_title="🌌 Asteroid & Comet Close Approaches Visualizer🌌", layout="wide")  
    st.title("🌠 Asteroid and Comet Close Approaches Visualizer🌠")  
    st.markdown("""
    Welcome to the **Asteroid and Comet Close Approaches Visualizer**! 🚀  
    Explore past and future close approaches of asteroids and comets to various celestial bodies.
    Use the sidebar to customize your search parameters and visualize the data interactively.
    """)
    
    
    st.sidebar.header("Input Parameters")  
    
    
    body_display_options = list(BODY_CODES.keys())  
    body_display = st.sidebar.selectbox(  
        "🪐 Select Celestial Body",  
        body_display_options,  
        index=2,  
        help="Choose the celestial body you want to analyze close approaches to."  
    )
    body_code = BODY_CODES[body_display]  
    
    
    st.sidebar.subheader("Date Range")  
    today = datetime.today()  
    default_end_date = today + timedelta(days=60)  
    
    date_min = st.sidebar.date_input(  
        "🔹 Start Date",  
        value=today,  
        min_value=datetime(1900, 1, 1),  
        max_value=datetime(2100, 12, 31),  
        help="Select the start date for the close approaches data."  
    )
    
    date_max_option = st.sidebar.selectbox(  
        "🔸 End Date Option",  
        options=['Days from Start Date', 'Specific Date'],  
        index=0,  
        help="Choose how to specify the end date for the data range."  
    )
    
    if date_max_option == 'Days from Start Date':  
        days_from_start = st.sidebar.number_input(  
            "📅 Number of Days from Start Date",  
            min_value=1,  
            max_value=36525,  
            value=60,  
            step=1,  
            help="Specify the number of days from the start date to set the end date."  
        )
        date_max = (datetime.combine(date_min, datetime.min.time()) + timedelta(days=days_from_start)).strftime('%Y-%m-%d')  
    elif date_max_option == 'Specific Date':  
        date_max_date = st.sidebar.date_input(  
            "📅 End Date",  
            value=default_end_date,  
            min_value=date_min,  
            max_value=datetime(2100, 12, 31),  
            help="Select a specific end date for the close approaches data."  
        )
        date_max = date_max_date.strftime('%Y-%m-%d')  
    
    
    st.sidebar.subheader("Distance Parameters")  
    dist_unit = st.sidebar.selectbox(  
        "📐 Distance Unit",  
        options=['AU', 'LD'],  
        index=0,  
        help="Choose the unit for maximum distance: Astronomical Units (AU) or Lunar Distances (LD)."  
    )
    default_dist_max = '0.05' if dist_unit == 'AU' else '10'  
    dist_max = st.sidebar.text_input(  
        "🔝 Maximum Distance",  
        value=default_dist_max,  
        help=f"Set the maximum distance for close approaches in {dist_unit}."  
    )
    
    
    st.sidebar.subheader("Object Type & Results")  
    object_type = st.sidebar.selectbox(  
        "☄️ Object Type",  
        options=['NEO', 'Comet', 'Both'],  
        index=0,  
        help="Filter results by object type: Near-Earth Objects (NEO), Comets, or Both."  
    )
    
    
    limit = st.sidebar.number_input(  
        "📈 Number of Results to Fetch",  
        min_value=1,  
        max_value=1000,  
        value=100,  
        step=1,  
        help="Specify how many close approach records to retrieve."  
    )
    
    
    fetch_data = st.sidebar.button("🚀 Fetch and Visualize Data")  
    
    if fetch_data:  
        with st.spinner("⏳ Fetching data..."):  
            if object_type in ['NEO', 'Comet']:  
                
                data = fetch_close_approaches(  
                    body_code=body_code,  
                    date_min=date_min.strftime('%Y-%m-%d'),  
                    date_max=date_max,  
                    dist_max=dist_max,  
                    dist_unit=dist_unit,  
                    limit=limit,  
                    object_type=object_type  
                )
                df = parse_data(data)  
            elif object_type == 'Both':  
                
                data_neo = fetch_close_approaches(  
                    body_code=body_code,  
                    date_min=date_min.strftime('%Y-%m-%d'),  
                    date_max=date_max,  
                    dist_max=dist_max,  
                    dist_unit=dist_unit,  
                    limit=limit,  
                    object_type='NEO'  
                )
                data_comet = fetch_close_approaches(  
                    body_code=body_code,  
                    date_min=date_min.strftime('%Y-%m-%d'),  
                    date_max=date_max,  
                    dist_max=dist_max,  
                    dist_unit=dist_unit,  
                    limit=limit,  
                    object_type='Comet'  
                )
                
                df_neo = parse_data(data_neo)  
                df_comet = parse_data(data_comet)  
                
                
                df = pd.concat([df_neo, df_comet], ignore_index=True)  
                df.drop_duplicates(inplace=True)  
        
        if not df.empty:  
            st.success(f"✅ Found {len(df)} close approaches to **{body_display}**.")  
            
            
            st.session_state['df'] = df  
            st.session_state['body_display'] = body_display  
            st.session_state['dist_unit'] = dist_unit  
        else:  
            st.session_state['df'] = pd.DataFrame()  
            st.session_state['body_display'] = body_display  
            st.session_state['dist_unit'] = dist_unit  
    
    
    if 'df' in st.session_state and not st.session_state['df'].empty:  
        df = st.session_state['df']  
        body_display = st.session_state['body_display']  
        dist_unit = st.session_state['dist_unit']  
        
        
        st.subheader("📊 Close Approach Data")  
        st.dataframe(df[['des', 'cd', 'dist', 'v_rel', 'v_inf']].rename(columns={  
            'des': '🪐 Designation',  
            'cd': '📅 Date',  
            'dist': f'📏 Distance ({dist_unit})',  
            'v_rel': '⚡ Relative Velocity (km/s)',  
            'v_inf': '∞ Infinity Velocity (km/s)'  
        }))  
        
        
        csv_data = df.to_csv(index=False).encode('utf-8')  
        st.download_button(  
            label="📥 Download Data as CSV",  
            data=csv_data,  
            file_name='close_approaches_data.csv',  
            mime='text/csv',  
        )
        
        
        st.markdown("---")  
        st.subheader("📈 Visualization")  
        add_trendline = st.checkbox("✨ Add Trendline (Requires statsmodels)")  
        
        
        visualize_close_approaches(df, body_display, add_trendline=add_trendline)  
    
    else:  
        if fetch_data:  
            st.info("ℹ️ No data available to display. Please adjust your search parameters.")  
        else:  
            st.info("🔍 Awaiting your search parameters. Use the sidebar to get started!")  
    
    st.markdown("""
    ---
    **🛰️ Data Source:** JPL's SSD/CNEOS CAD API 
    """)

if __name__ == '__main__':  
    main()  
