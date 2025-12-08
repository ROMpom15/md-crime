import plotly.io as pio

# 1. Load the figure from the saved JSON file
try:
    fig = pio.read_json("campus_crime_choropleth.json")
    
    # 2. Save the figure as a static HTML file for easy, interactive viewing.
    html_file_name = "campus_crime_choropleth_interactive.html"
    fig.write_html(html_file_name)
    
    print(f"The interactive Choropleth map has been successfully generated and saved as {html_file_name}")
    print("Download and open this HTML file in a web browser to view the animated map.")
    
except FileNotFoundError:
    print("Error: The file 'campus_crime_choropleth.json' was not found. Please ensure the aggregation step ran successfully.")
except Exception as e:
    print(f"An error occurred while loading or saving the figure: {e}")