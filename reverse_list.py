#!/usr/bin/env python3


def revlist(l):
    ll = len(l)
    #print("len of list = {}".format(ll))

    for i in range(ll//2):
        temp = l[i]
        last =  - (i + 1)
        l[i] = l[last]
        l[last] = temp
        #print("temp: {} i: {} last: {} l[-last]: {} list: {}".format(temp, i, last, l[-last], l))
        #print(l)



def main():
  mylist = ["person", "woman", "man", "camera", "tv"]

  print(mylist)

  revlist(mylist)

  print(mylist)


if __name__ == '__main__':
    main()
