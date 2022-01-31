import pandas as pd
from selenium import webdriver

class Crawler:
    def __init__(self):
        self.title_list = list()
        self.singer_list = list()
        self.lyrics_list = list()

    def data_to_pd(self):
        print(len(self.title_list), len(self.singer_list), len(self.lyrics_list))   
        df = pd.DataFrame({'제목':self.title_list, '가수':self.singer_list, '가사': self.lyrics_list})
        print(df)

    def crawler_melon_chart(self,index):
        driver = webdriver.Chrome(executable_path='chromedriver')
        driver.get("https://www.melon.com/genre/song_list.htm?gnrCode=GN0100#params%5BgnrCode%5D=GN0100&params%5BdtlGnrCode%5D=&params%5BorderBy%5D=POP&params%5BsteadyYn%5D=N&po=pageObj&startIndex={}".format(index))

        song_num_list = list()
        song_num = driver.find_elements_by_xpath("//button[@data-song-no]")

        for song in song_num:
            song_id = song.get_attribute('data-song-no') 
            song_num_list.append(song_id)
            
        print(len(song_num_list))

        for song_id in song_num_list:
            driver.get("https://www.melon.com/song/detail.htm?songId=" + song_id)
            try:
                title = driver.find_element_by_class_name('song_name').text
                self.title_list.append(title)
                singer = driver.find_element_by_class_name('artist_name').get_attribute('title')
                self.singer_list.append(singer)
                lyrics = driver.find_element_by_class_name('lyric').text
                self.lyrics_list.append(lyrics) 
            except:
                pass    

if __name__ == "__main__":
    page_list = [1,51]

    crawler = Crawler()
    for page in page_list:
        crawler.crawler_melon_chart(page)

    crawler.data_to_pd()
