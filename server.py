from flask import Flask, request, render_template, send_from_directory, abort
from weather import get_current_weather
from waitress import serve

app=Flask(__name__, static_url_path='/static')

@app.route('/')
@app.route('/index')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        app.logger.error(f"Error rendering template: {e}")
        abort(500)

# @app.route('/static/<path:path>')
# def send_static(path):
#     return send_from_directory('static', path)

@app.route('/weather')
def get_weather():
    city=request.args.get('city')
    
    if not bool(city.strip()):
        city="Visakhapatnam"
    
    weather_data=get_current_weather(city)
    
    if not weather_data["cod"]==200:
        return render_template('city_not_found.html')
    
    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )

if __name__ == "__main__":
    serve(app, host="0.0.0.0",port="8000")