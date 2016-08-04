import requests
from bs4 import BeautifulSoup

url = "http://www.espncricinfo.com/ci/engine/match/index.html?view=live"
match_status = []
def open_url(url):
    return requests.get(url).text  # returns html

def get_bsoup_object(html):
    return BeautifulSoup(html, "html.parser")  # returns soup (BeautifulSoup's object)

def get_team_divs(soup):
    teams1 = soup.find_all('div', attrs = {'class': 'innings-info-1'})
    teams2 = soup.find_all('div', attrs = {'class': 'innings-info-2'})
    matches = soup.find('section',{'id':'live-match-data'})
    for match in matches.find_all('section',{'class':'default-match-block'}):
		
		status = match.find('div',{'class':'match-status'})
                status_info = status.find('span').get_text()
                match_status.append(status_info[0:75])
    return get_team_scores(teams1), get_team_scores(teams2), match_status

def get_team_scores(team_soup):
    team = list(map(lambda x: x.contents, team_soup))
    for t in team:
        t[1] = t[1].contents
    return [[t[0].strip(), t[1]] for t in team]

def main():
    t1, t2, m = get_team_divs(get_bsoup_object(open_url(url)))
    for i in range(len(t1)):
        print "%s. %s %s VS %s %s %s" %(i+1, t1[i][0], t1[i][1], t2[i][0], t2[i][1], m[i])
if __name__ == "__main__":
	main()
