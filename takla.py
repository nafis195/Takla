import enchant # pip3 install pyenchant
from langdetect import detect # pip3 install langdetect
from langdetect import DetectorFactory
DetectorFactory.seed = 0

d = enchant.Dict('en_US')
def takla(word):   
    if d.check(word) is False:
        if detect(word) is 'bn':
            return 0
        else:
            return 1
    else:
        return 0

def main():
    string = str(input())
    words = string.split()
    ans = 0
    for word in words:
        ans += takla(word)
    if ans > 0:
        print('Takla? Yeah!!!')
    else:
        print('Takla? Nope!!!')


if __name__ == '__main__':
	main()
