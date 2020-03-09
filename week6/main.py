import cli

if __name__ == "__main__":
    cli.manager()

'''
CLI commands

main.py command --download url
main.py command --avg text

(hardest read is part of the command below)
main.py multi url1 url2 url3 etc
    example: 
        main.py multi https://raw.githubusercontent.com/IronLanguages/ironpython3/master/README.md https://raw.githubusercontent.com/datsoftlyngby/dat4sem2020spring-python/master/06%20Exercise.ipynb https://www.albinoblacksheep.com/text/bloodninja
        
ex2

1. 
    main.py multi https://www.gutenberg.org/files/1342/1342-0.txt https://www.gutenberg.org/files/1934/1934-0.txt https://www.gutenberg.org/files/41/41-0.txt https://www.gutenberg.org/cache/epub/972/pg972.txt https://www.gutenberg.org/files/2600/2600-0.txt https://www.gutenberg.org/files/1250/1250-0.txt https://www.gutenberg.org/files/2591/2591-0.txt https://www.gutenberg.org/files/43/43-0.txt https://www.gutenberg.org/cache/epub/5200/pg5200.txt https://www.gutenberg.org/files/1952/1952-0.txt
        
'''
