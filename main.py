from playwright.sync_api import sync_playwright
import time
import datetime

def get_weekday_food(text_input):
    weekdays = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag"]
    day = weekdays[datetime.date.today().weekday()]

    rows = text_input.split('\n')
    found = False
    for row in rows:
        if found:
            print(row)
            break
        if day in row:
            found = True

def get_orangeriet_food(text_input):
    weekdays = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag"]
    day = weekdays[datetime.date.today().weekday()]
    next_day = weekdays[datetime.date.today().weekday() + 1]
    #print(day)
    rows = text_input.split('\n')

    found = False
    index = 0
    for row in rows:
        if index < 3:
            index += 1
            continue
        if found:
            if next_day in row:
                found = False
                break
            print(row)

        if day in row:
            found = True
            print(row)
        index += 1

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://mattiasmat.se/cafeet-i-vaxthuset/")

    growhouse_selector = 'div.entry-content:nth-child(2) div'
    orangeriet_selector = 'div.lunch-content'

    print("Växthuset: ")
    monday_text = page.query_selector(growhouse_selector).text_content()
    get_weekday_food(monday_text)

    print("\nOrangeriet: ")
    orangeriet_text = page.query_selector(orangeriet_selector).text_content()
    get_orangeriet_food(orangeriet_text)

    browser.close()
