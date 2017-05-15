__author__ = 'elizajasin'

import re
import operator

def tagging (data):
    #create bag of words for emission probability using unigram model
    bagOfWords_time = {}
    bagOfWords_loc = {}
    bagOfWords_speak = {}
    for i in range(len(data)):
        #search the pattern of each class from data using regex
        match_time = re.search(r'<stime>(.+)</stime>',data[i])
        match_location = re.search(r'<location>(.+)</location>',data[i])
        match_speaker = re.search(r'<speaker>(.+)</location>',data[i])
        #count all words with its tag
        if match_time != None:
            words_time = str(match_time.groups()[0]).split()
            for j in range(len(words_time)):
                if words_time[j] in bagOfWords_time.keys():
                    bagOfWords_time[words_time[j]] = bagOfWords_time[words_time[j]]+1
                else:
                    bagOfWords_time[words_time[j]] = 1
        if match_location != None:
            words_loc = str(match_location.groups()[0]).split()
            for j in range(len(words_loc)):
                if words_loc[j] in bagOfWords_loc.keys():
                    bagOfWords_loc[words_loc[j]] = bagOfWords_loc[words_loc[j]]+1
                else:
                    bagOfWords_loc[words_loc[j]] = 1
        if match_speaker != None:
            words_speaker = str(match_speaker.groups()[0]).split()
            for j in range(len(words_speaker)):
                if words_speaker[j] in bagOfWords_speak.keys():
                    bagOfWords_speak[words_speaker[j]] = bagOfWords_speak[words_speaker[j]]+1
                else:
                    bagOfWords_speak[words_speaker[j]] = 1
    return bagOfWords_time,bagOfWords_loc,bagOfWords_speak

def emission_probability(bagOfWords_time,bagOfWords_loc,bagOfWords_speak):
    #sum all words in each class
    sum_time = sum(bagOfWords_time.values())
    sum_loc = sum(bagOfWords_loc.values())
    sum_speak = sum(bagOfWords_speak.values())
    #count emission probability
    ep_time = {}
    ep_loc = {}
    ep_speak = {}
    for key in bagOfWords_time:
        ep_time[key] = bagOfWords_time[key]/sum_time
    for key in bagOfWords_loc:
        ep_loc[key] = bagOfWords_loc[key]/sum_loc
    for key in bagOfWords_speak:
        ep_speak[key] = bagOfWords_speak[key]/sum_speak
    return ep_time,ep_loc,ep_speak