"""
File: webcrawler.py
Name: 許景涵
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features='html.parser')

        # ----- Write your code below this line ----- #
        # The structure: <table class='t-stripe'> -> <tbody> -> <tr> -> <td>
        tbody = soup.find('tbody')

        # Initialize male and female total numbers
        male_total = 0
        female_total = 0

        if tbody:
            tags = tbody.find_all('tr')

            for tag in tags:
                target = tag.find_all('td')

                # Ensure that there are at least 5 cells <td> in a row <tr>
                if len(target) >= 5:
                    # Number of males is from the element at index 2.
                    # Remove commas from the text and convert it to an integer.
                    male_number = int(target[2].text.replace(',', ''))
                    # Number of females is from the element at index 4
                    female_number = int(target[4].text.replace(',', ''))

                    male_total += male_number
                    female_total += female_number

        print(f"Male Number: {male_total}")
        print(f"Female Number: {female_total}")


if __name__ == '__main__':
    main()
