# Fetching mini-league data using json

# Importing
import requests
from prettytable import PrettyTable
from prettytable import MSWORD_FRIENDLY

# Function start
def minileague():

    # Asking League ID and Pages
    ml_id = input('Enter the mini-league ID: ')

    # Uncomment the section below if you want to know the number of pages in your mini-league

    # i_pages = 1
    # urla = "https://fantasy.premierleague.com/drf/leagues-classic-standings/%s?phase=1&le-page=1&ls-page=%s" % (ml_id,i_pages)
    # json_pages = requests.get(urla).json()
    # # print(len(json_pages['standings']['results']))
    # print("Calculating total number of pages...")
    #
    # while len(json_pages['standings']['results']) >= 49:
    #     i_pages=i_pages+1
    #     urla = "https://fantasy.premierleague.com/drf/leagues-classic-standings/%s?phase=1&le-page=1&ls-page=%s" % (ml_id, i_pages)
    #     json_pages = requests.get(urla).json()
    # else:
    #     print("This mini league has %s pages" %(i_pages))

    # Uncomment the section above if you want to know the number of pages in your mini-league


    frompage = int(input('Enter from page number: '))
    topage = int(input('Enter to page number: '))

    # Table headers
    headers = ['Rank','Last Rank','Team Name','Total','GW Pts', 'Bench Pts','GW TR','Cost','Total TR',
               'Value','ITB','Total V','Captain','ViceCap','Chip1','Chip2','Chip3','Chip4','Chip5','Team ID']
    table = PrettyTable(headers)

    # Fetching Gameweek Number
    url0 = "https://fantasy.premierleague.com/drf/bootstrap-static"
    json_bootstrap = requests.get(url0).json()
    gw = json_bootstrap['current-event']
    event = gw-1

    # Fetching Player Data
    url3 = 'https://fantasy.premierleague.com/drf/bootstrap-static'
    json_live = requests.get(url3).json()

    # Import all player data in premier league
    player_d = {}
    for each in json_live['elements']:
        pl_position = each['element_type']
        pl_id = each['id']
        pl_name = each['web_name']
        player_d[pl_id] = pl_name
    tot_player = len(player_d)
    # print(tot_player)
    # print(player_d[23])

    # Fetching league url with given page numbers
    for key1 in range(frompage,topage+1):

        url1 = "https://fantasy.premierleague.com/drf/leagues-classic-standings/%s?phase=1&le-page=1&ls-page=%s" % (ml_id,key1)
        json_minileague = requests.get(url1).json()
        print("https://fantasy.premierleague.com/a/leagues/standings/%s/classic?phase=1&lsPage=%s&lePage=1" % (ml_id, key1))
        print('Please be patient; loading tabular data for page %s...' % (key1))

        # Fetching details
        for each in json_minileague['standings']['results']:
            team_name = each['entry_name']
            team_id = each['entry']
            gw_points = each['event_total']
            total_points = each['total']
            current_rank = each['rank']
            last_rank = each['last_rank']
            data = [current_rank,last_rank,team_name,total_points,gw_points]

            # Fetching individual team data
            url2 = "https://fantasy.premierleague.com/drf/entry/%s/history" % (team_id)
            json_history = requests.get(url2).json()
            gwplayed = int(len(json_history['history'])-1)

            # Points benched
            points_benched = json_history['history'][gwplayed]['points_on_bench']
            data.append(points_benched)

            # Transfers Made / Cost
            transfers_made = json_history['entry']['event_transfers']
            transfers_cost = json_history['entry']['event_transfers_cost']
            total_transfers = json_history['entry']['total_transfers']
            data.append(transfers_made)
            data.append(transfers_cost)
            data.append(total_transfers)

            # Team Values
            team_value = json_history['entry']['value']
            tv = team_value/10
            in_the_bank = json_history['entry']['bank']
            itb = in_the_bank/10
            total_value = (tv+itb)
            data.append(tv)
            data.append(itb)
            data.append("%.1f" % total_value)

            url4 = "https://fantasy.premierleague.com/drf/entry/%s/event/%s/picks" % (team_id, gw)
            # print(url4)

            json_pick = requests.get(url4).json()
            for each1 in json_pick['picks']:
                player_id = each1['element']
                captain = each1['is_captain']
                vicecapt = each1['is_vice_captain']
                multiplier = each1['multiplier']
                pl_name = player_d[player_id]
                plist = {player_id: pl_name}
                player_idnew = str(player_id)

                if captain == True:
                    data.append(pl_name)

            for each1 in json_pick['picks']:
                player_id = each1['element']
                captain = each1['is_captain']
                vicecapt = each1['is_vice_captain']
                multiplier = each1['multiplier']
                pl_name = player_d[player_id]
                plist = {player_id: pl_name}
                player_idnew = str(player_id)

                if vicecapt == True:
                    data.append(pl_name)

            # Chips Used
            if len(json_history['chips']) == 1:
                for each in json_history['chips']:
                    chipname = each['name']
                    data.append(chipname)
                data.append("n/a")
                data.append("n/a")
                data.append("n/a")
                data.append("n/a")
            elif len(json_history['chips']) == 2:
                for each in json_history['chips']:
                    chipname = each['name']
                    data.append(chipname)
                data.append("n/a")
                data.append("n/a")
                data.append("n/a")
            elif len(json_history['chips']) == 3:
                for each in json_history['chips']:
                    chipname = each['name']
                    data.append(chipname)
                data.append("n/a")
                data.append("n/a")
            elif len(json_history['chips']) == 4:
                for each in json_history['chips']:
                    chipname = each['name']
                    data.append(chipname)
                data.append("n/a")
            elif len(json_history['chips']) == 5:
                for each in json_history['chips']:
                    chipname = each['name']
                    data.append(chipname)
            else:
                data.append("n/a")
                data.append("n/a")
                data.append("n/a")
                data.append("n/a")
                data.append("n/a")

            data.append(team_id)

            # table.set_style(MSWORD_FRIENDLY)			# Uncomment if you want to be able to copy/paste the table

            table.add_row(data)
    # Printing Table
    print(table)

# Executing Function
minileague()