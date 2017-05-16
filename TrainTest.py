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
        match_speaker = re.search(r'<speaker>(.+)</speaker>',data[i])
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

def train(data,n):
    # training process
    data_train = []
    for i in range(n):
        data_train.append(data[i])
    bagOfWords_time,bagOfWords_loc,bagOfWords_speak = tagging(data_train)
    return emission_probability(bagOfWords_time,bagOfWords_loc,bagOfWords_speak)

def tes(data,n,ep_time,ep_loc,ep_speak):
    # testing process
    true_time = 0
    test_time = 0
    true_loc = 0
    tes_loc = 0
    true_speak = 0
    tes_speak = 0
    data_test = []
    for i in range(n,len(data)):
        data_test.append(data[i])
    for i in range(len(data_test)):
        #search the pattern of each class from data using regex
        match_time = re.search(r'<stime>(.+)</stime>',data[i])
        match_location = re.search(r'<location>(.+)</location>',data[i])
        match_speaker = re.search(r'<speaker>(.+)</speaker>',data[i])
        if match_time != None:
            test_time += 1
            time = str(match_time.groups()[0]).split();
            for i in range(len(time)):
                prob = {}
                if time[i] in ep_time.keys():
                    if "time" in prob.keys():
                        if prob["time"] < ep_time[time[i]]:
                            prob["time"] = ep_time[time[i]]
                    else:
                        prob["time"] = ep_time[time[i]]
                if time[i] in ep_loc.keys():
                    if "loc" in prob.keys():
                        if prob["loc"] < ep_time[time[i]]:
                            prob["loc"] = ep_time[time[i]]
                    else:
                        prob["loc"] = ep_time[time[i]]
                if time[i] in ep_speak.keys():
                    if "speak" in prob.keys():
                        if prob["speak"] < ep_time[time[i]]:
                            prob["speak"] = ep_time[time[i]]
                    else:
                        prob["speak"] = ep_time[time[i]]
            if max(prob.values()) == prob["time"]:
                true_time += 1
        if match_location != None:
            tes_loc += 1
            loc = str(match_location.groups()[0]).split();
            for i in range(len(loc)):
                prob = {}
                if loc[i] in ep_time.keys():
                    if "time" in prob.keys():
                        if prob["time"] < ep_time[loc[i]]:
                            prob["time"] = ep_time[loc[i]]
                    else:
                        prob["time"] = ep_time[loc[i]]
                if loc[i] in ep_loc.keys():
                    if "loc" in prob.keys():
                        if prob["loc"] < ep_loc[loc[i]]:
                            prob["loc"] = ep_loc[loc[i]]
                    else:
                        prob["loc"] = ep_loc[loc[i]]
                if loc[i] in ep_speak.keys():
                    if "speak" in prob.keys():
                        if prob["speak"] < ep_loc[loc[i]]:
                            prob["speak"] = ep_loc[loc[i]]
                    else:
                        prob["speak"] = ep_loc[loc[i]]
            if max(prob.values()) == prob["loc"]:
                true_loc += 1
        if match_speaker != None:
            tes_speak += 1
            speak = str(match_speaker.groups()[0]).split();
            for i in range(len(speak)):
                prob = {}
                if speak[i] in ep_time.keys():
                    if "time" in prob.keys():
                        if prob["time"] < ep_speak[speak[i]]:
                            prob["time"] = ep_speak[speak[i]]
                    else:
                        prob["time"] = ep_speak[speak[i]]
                if speak[i] in ep_loc.keys():
                    if "loc" in prob.keys():
                        if prob["loc"] < ep_speak[speak[i]]:
                            prob["loc"] = ep_speak[speak[i]]
                    else:
                        prob["loc"] = ep_speak[speak[i]]
                if speak[i] in ep_speak.keys():
                    if "speak" in prob.keys():
                        if prob["speak"] < ep_speak[speak[i]]:
                            prob["speak"] = ep_speak[speak[i]]
                    else:
                        prob["speak"] = ep_speak[speak[i]]
            if max(prob.values()) == prob["speak"]:
                true_speak += 1
    return test_time,tes_loc,tes_speak,true_time,true_loc,true_speak

def akurasi (test_time,tes_loc,tes_speak,true_time,true_loc,true_speak):
    test = test_time+tes_loc+tes_speak
    true = true_time+true_loc+true_speak
    accuracy = true/test*100
    return (str(accuracy)+'%')