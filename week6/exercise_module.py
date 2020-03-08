from exceptions import NotFoundException
import requests
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import multiprocessing
import re


class ExerciseModule():
    __file_name_list = []

    def __init__(self, url_list):
        self.__url_list = url_list

    @staticmethod
    def download(url, filename):
        '''
        2. download(url,filename) raises NotFoundException when url returns 404
        '''
        try:
            r = requests.get(url)
            r.raise_for_status()
            with open(filename, 'wb') as fileWrite:
                for chunk in r.iter_content(chunk_size=1024):
                    fileWrite.write(chunk)
        except requests.exceptions.HTTPError as error:
            raise NotFoundException(str(error))

    def __name_handle(self, s):
        s = s.replace(s.split('.')[-1], '')
        s = s.replace('.', '')

        return s.split('/')[-1]

    def __dl_append(self, url):
        try:
            r = requests.get(url)
            r.raise_for_status()
            name = self.__name_handle(url)
            self.__file_name_list.append(name)
            with open(name + '.txt', 'ab') as fileAppend:
                fileAppend.flush()
                for chunk in r.iter_content(chunk_size=1024):
                    fileAppend.write(chunk)
        except requests.exceptions.HTTPError as error:
            raise NotFoundException(str(error))

    def multi_download(self, url_list):
        '''
        3. multi_download(url_list) uses threads to download multiple urls as text and stores filenames as a property
        '''
        with ThreadPoolExecutor() as executor:
            for url in url_list:
                executor.map(self.__dl_append(url))

    def __iter__(self):
        '''
        4. iter() returns an iterator

        I'm going to presume that this is referring to an iterator of the url list
        '''
        self.num = 0
        return self

    def __next__(self):
        '''
        5. next() returns the next filename (and stops when there are no more)
        '''
        if(self.num <= len(self.__file_name_list)):
            res = self.__file_name_list[self.num]
            self.num += 1
            return res
        else:
            raise StopIteration

    def url_list_generator(self):
        '''
        6. urllist_generator() returns a generator to loop through the urls

        '''

        def gen(self):
            for url in self.__url_list:
                yield url
        return gen()

    def avg_vowels(self, text):
        '''
        7. avg_vowels(text) - a rough estimate on readability returns average number of vowels in the words of the text

        I am going to assume that this is referring to a text file and not a string
        '''
        with open(text, 'r') as fileRead:
            line_count = 0
            total = 0
            for line_count, line in enumerate(fileRead.readlines()):
                word_count = 0
                val = 0
                for word_count, word in enumerate(line.split(' ')):
                    pre = len(word)
                    cut = re.sub(pattern='[aeioyu]', repl='',
                                 string=word, flags=re.IGNORECASE, count=0)
                    val += pre - len(cut)
                if(word_count != 0):
                    total += val/word_count
            return total/line_count

    def hardest_read(self):
        iterator = self.iter()
        avg_vowels(iterator.next())
        generator = url_list_generator

        '''
        hardest_read() returns the filename of the text with the highest vowel score (use all the cpu cores on the computer for this work.
        '''
        raise NotImplemented

    @property
    def url_list(self):
        return self.__url_list

    @url_list.setter
    def url_list(self, ul):
        self.__url_list = ul

    @property
    def file_name_list(self):
        return self.__file_name_list

    @file_name_list.setter
    def file_name_list(self, flist):
        self.__file_name_list = flist
