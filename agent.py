# ============================================
# PPC Real Estate Auto-Posting Agent (Simple API Version)
# ============================================

from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# ---- STEP 1 SCRAPE PROPERTY ----
def scrape_property(url str) - dict
    headers = {User-Agent Mozilla5.0}
    r = requests.get(url, headers=headers, timeout=15)
    soup = BeautifulSoup(r.text, html.parser)

    title = soup.find(h1).get_text(strip=True) if soup.find(h1) else Property
    description = 

    desc_el = soup.find(class_=lambda c c and description in c.lower())
    if desc_el
        description = desc_el.get_text( , strip=True)[500]

    return {
        title title,
        description description,
        url url
    }

# ---- STEP 2 GENERATE SIMPLE POSTS (NO API KEY NEEDED) ----
def generate_posts(property_data: dict) -> dict:
    title = property_data["title"]
    url = property_data["url"]

    return {
        "facebook": f"New Property Alert!\n\n{title}\n\nExplore this amazing opportunity today.\n\nContact us for details.\n{url}",
        "instagram": f"{title}\n\nDM for details\n\n#PPCRealEstate #PropertyForSale",
        "youtube": {
            "title": f"{title} | PPC Real Estate",
            "description": f"Explore {title}. Contact us today.\n{url}"
        },
        "gmb": f"New property listed: {title}. Contact us for more info.\n{url}"
    }

# ---- API ROUTES ----

@app.route(, methods=[GET])
def home()
    return ✅ PPC Agent is LIVE!

@app.route(run, methods=[POST])
def run()
    data = request.json
    url = data.get(url)

    if not url
        return jsonify({error URL is required}), 400

    try
        property_data = scrape_property(url)
        posts = generate_posts(property_data)

        return jsonify({
            status success,
            property property_data,
            posts posts
        })
    except Exception as e
        return jsonify({error str(e)}), 500


# ---- RUN SERVER ----
if __name__ == __main__
    app.run(host=0.0.0.0, port=5000)
