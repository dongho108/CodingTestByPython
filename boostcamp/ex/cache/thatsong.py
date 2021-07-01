import math


def solution(m, musicinfos):
    answer = ''

    music = dict()

    for musicinfo in musicinfos:
        info = musicinfo.split(',')

        musiclen = timesub(info[1], info[0])
        musicname = info[2]
        musicsheet = info[3]

        if musiclen > len(info[3]):
            for i in range(math.ceil(musiclen / len(info[3]))):
                musicsheet += musicsheet
        musicsheet = musicsheet[:musiclen - 1]

        music[musicname] = musicsheet

    print(music)

    return answer