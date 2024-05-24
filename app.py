import requests
from bs4 import BeautifulSoup
from flask import Flask , render_template, request , jsonify , send_file
from flask_cors import CORS
from moviepy.editor import ImageClip 
import moviepy.editor as mp
from urllib.request import urlopen
import io



app = Flask(__name__)

CORS(app , origins=["http://localhost:3000"])


url = "https://www.google.com/search?sca_esv=dd1ffd98a4eb7379&sca_upv=1&sxsrf=ADLYWIK82eK9MavnNKBNwBC5bOfmKboOow:1715065713442&q=Tajmahal&uds=ADvngMh2Gsd1U95AqRLv_MuIJ9BifU-x9Kl7hMdSYydccVixFhALDrqnE7Mjx1wzLJPxSZWrJNvH89L3ZzMTN-AxuMEwUdToHXB4nJBRM649j9RG0cMt7GBgFrQWNJSVloppztHNsbussf31UE53cmEepd2xDJqDn3lXM-mNUQYKpvcZwBPyimjHBpMbCj6-YyylFxdAVytFo6H-2Stt-FGLd1NjhuKzOZZoE9ZI3TZlx3jigKWoMSfDflF30o6LVKrs9zCdqcFdcC22BLZZj_5j06zGoZ1JSR71ufjZKK5o05m63WoyO_E&udm=2&prmd=invsmbtz&sa=X&ved=2ahUKEwi1yvbU_fqFAxWTTGwGHVP1BXYQtKgLegQIERAB&biw=1280&bih=585&dpr=1.5"

def get_html_code(url):
 
  try:
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for unsuccessful requests

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Return the parsed HTML content
    li = soup.find_all('img')

    last_li = []

    for tag in li:
      last_li.append(tag.get('src'))

    return last_li  

  except requests.exceptions.RequestException as e:
    raise Exception(f"Error fetching webpage: {e}")

# Example usage  
@app.route('/')
def home():
  return 'I am ready'


@app.route('/related_images' , methods = ['POST'])
def scrape():
  query = request.form['query']
  url  = (f"https://www.google.com/search?sca_esv=dd1ffd98a4eb7379&sca_upv=1&sxsrf=ADLYWIK82eK9MavnNKBNwBC5bOfmKboOow:1715065713442&q={query}&uds=ADvngMh2Gsd1U95AqRLv_MuIJ9BifU-x9Kl7hMdSYydccVixFhALDrqnE7Mjx1wzLJPxSZWrJNvH89L3ZzMTN-AxuMEwUdToHXB4nJBRM649j9RG0cMt7GBgFrQWNJSVloppztHNsbussf31UE53cmEepd2xDJqDn3lXM-mNUQYKpvcZwBPyimjHBpMbCj6-YyylFxdAVytFo6H-2Stt-FGLd1NjhuKzOZZoE9ZI3TZlx3jigKWoMSfDflF30o6LVKrs9zCdqcFdcC22BLZZj_5j06zGoZ1JSR71ufjZKK5o05m63WoyO_E&udm=2&prmd=invsmbtz&sa=X&ved=2ahUKEwi1yvbU_fqFAxWTTGwGHVP1BXYQtKgLegQIERAB&biw=1280&bih=585&dpr=1.5")
  html_code = get_html_code(url)
  html_code.pop(0)
  return html_code




@app.route('/video' , methods = ['GET','POST'])
def video():
          clips = []
          image_urls = request.get_json() 
          image_urls = image_urls[1::]
          for url in image_urls:
              try:
         
                  image_data = urlopen(url).read()
                  temp_file = io.BytesIO(image_data)
                  clip = mp.ImageClip(temp_file).set_duration(3)
                  clips.append(clip)
              except Exception as e:
                  print(f"Error downloading image from {url}: {e}")

          # Concatenate clips with transitions (optional)
          final_clip = mp.concatenate_videoclips(clips, method='compose')  # Adjust 'compose' for desired transitions

          # Write the final video
          final_clip.write_videofile("output_video.mp4", fps=24)  # Adjust fps as needed
          

     

if __name__ == '__main__':
  app.run(host = '0.0.0.0', debug=True)
