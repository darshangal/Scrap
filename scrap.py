import requests
from bs4 import BeautifulSoup
import sqlite3
conn = sqlite3.connect('mydatabase.db')

# Send an HTTP GET request to the website
url = 'https://ipowatch.in/ipo-grey-market-premium-latest-ipo-gmp/'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser',from_encoding='utf-8')
    
    # Extract and print the quotes and authors
    tables = soup.find_all('figure', class_='wp-block-table')
    table = tables[0]
    body = table.find('tbody')
    rows = body.find_all('tr')
    data =[]

    cursor = conn.cursor()

    

    for row in rows:
        columns = row.find_all('td')
        name = columns[0]
        type = columns[1]
        gmp = columns[2]
        price = columns[3]
        gain = columns[4]
        description = name.find('a')
        description.extract()
        data.append(
            {
                "Name":description.text,
                "Type":type.get_text().replace('\xa0', ' '),
                "GMP": gmp.text,
                "Price":price.text,
                "gain":gain.text,
                "Duration":name.text
            }
        )
        # Define an SQL command to create a table
        type_desc=type.get_text().replace('\xa0', ' ')
        create_table_query = f"""
        INSERT INTO IpoData (
            Name,
            Type,
            GMP,
            Price,
            Gain,
            Duration
        )
        VALUES
        (
        '{description.text}',
        '{type_desc}',
        '{gmp.text}',
        '{price.text}',
        '{gain.text}',
        '{name.text}'
        )
        """

        # Execute the SQL command to create the table
        cursor.execute(create_table_query)
    # Commit the changes and close the database connection
    conn.commit()
    conn.close()

    print(data)
else:
    print(f'Failed to retrieve the web page. Status code: {response.status_code}')
