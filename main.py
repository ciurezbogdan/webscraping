from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from bs4 import BeautifulSoup
from handlers.data import write_output, parse_colors
from handlers.drivers import accept_cookies

source = 'https://htmlcolorcodes.com/'

if __name__ == '__main__':
    # deprecated driver = webdriver.Edge(executable_path=r"C:\things\Python\webdrivers\NewEdge\msedgedriver.exe")
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

driver.get(source)
accept_cookies(driver)
soup = BeautifulSoup(driver.page_source, features='html.parser')
colors = parse_colors(soup)
write_output(source, colors)

driver.close()
