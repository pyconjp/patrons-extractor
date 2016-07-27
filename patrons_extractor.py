import requests
from jinja2 import Template
from bs4 import BeautifulSoup


LINE_BREAK_SIZE = 5
PARTICIPANTS_PAGE_URL = 'http://pyconjp.connpass.com/event/30692/participation/'
PATRON_TEMPLATE = """
====================
Patronスポンサー
====================

.. raw:: html

   <div style="width:100%; display:table; border-collapse: separate; border-spacing: 0 12px;">
       <div style="display: table-row; width: 100%;">
       {% for patron in patrons %}
           <div style="display: table-cell; width: 20%;">
               <div style="margin: 0 auto; width: 100%;">
                   <div><img src="{{ patron['icon'] }}"><br>{{ patron['name'] }}</div>
                   <div style="display:table; border-collapse: separate; border-spacing: 4px 0;">
                       <div style="display: table-cell; width: 33%;">
                           {% if patron['twitter'] %}
                           <a href="{{ patron['twitter'] }}"><img src="https://connpass.com/static/img/common/icon_twitter.png"></a>
                           {% else %}
                           <img src="https://connpass.com/static/img/common/icon_twitter.png" style="opacity:0.2" >
                           {% endif %}
                       </div>
                       <div style="display: table-cell; width: 33%;">
                           {% if patron['facebook'] %}
                           <a href="{{ patron['facebook'] }}"><img src="https://connpass.com/static/img/common/icon_facebook.png"></a>
                           {% else %}
                           <img src="https://connpass.com/static/img/common/icon_facebook.png" style="opacity:0.2" >
                           {% endif %}
                       </div>
                       <div style="display: table-cell; width: 33%;">
                           {% if patron['github'] %}
                           <a href="{{ patron['github'] }}"><img src="https://connpass.com/static/img/common/icon_github.png"></a>
                           {% else %}
                           <img src="https://connpass.com/static/img/common/icon_github.png" style="opacity:0.2" >
                           {% endif %}
                       </div>
                   </div>
               </div>
           </div>
           {% if loop.index % break_line_size == 0 %}</div><div style="display: table-row; width: 100%;">{% endif %}
        {% endfor %}
        </div>
   </div>
"""


def _make_soup(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    return soup


def _extract_patrons(soup):
    patron_table = soup.find(string="Patron").find_parents("table")
    assert len(patron_table) == 1, "scraping error"
    patrons = patron_table[0].tbody.find_all('tr')
    return patrons


def _extract_social_url(social_urls, service_domain):
    for social_url in social_urls:
        if service_domain in social_url:
            return social_url


def _parse_patron_soup(patron_soup):
    social_soups = patron_soup.find('td', attrs={'class': 'social'}).find_all('a')
    social_urls = [x.get('href') for x in social_soups]
    twitter_url = _extract_social_url(social_urls, 'twitter')
    facebook_url = _extract_social_url(social_urls, 'facebook')
    github_url = _extract_social_url(social_urls, 'github')

    return {
        'name': patron_soup.find('p', attrs={'class': 'display_name'}).a.text,
        'icon': patron_soup.find('a', attrs={'class': 'image_link'}).img.get('src'),
        'twitter': twitter_url,
        'facebook': facebook_url,
        'github': github_url,
    }


if __name__ == '__main__':
    soup = _make_soup(PARTICIPANTS_PAGE_URL)
    patron_soups = _extract_patrons(soup)

    patrons = []

    for patron_soup in patron_soups:
        patrons.append(_parse_patron_soup(patron_soup))

    template = Template(PATRON_TEMPLATE)
    patron_html = template.render(patrons=patrons, break_line_size=LINE_BREAK_SIZE)
    print(patron_html)
