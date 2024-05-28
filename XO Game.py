#!/usr/bin/env python
# coding: utf-8

# In[17]:


def emptyList_XO():
    tmp_lst =[]
    for i in range(9):
        tmp_lst.append(' ')
    return tmp_lst


# In[18]:


XO_list=emptyList_XO()


# In[19]:


def printBoard(XOList):
    print(XOList[0], "|",XOList[1], "|",XOList[2])
    print("----------")
    print(XOList[3], "|",XOList[4], "|",XOList[5])
    print("----------")
    print(XOList[6], "|",XOList[7], "|",XOList[8])


# In[20]:


printBoard(XO_list)


# In[21]:


import random
def whowillGoFirst():
    player=random.randint(0,1)
    if player==0:
        print("player A will go first")
    else:
        print("player B will go first")
    return player


# In[27]:


def takeInput(player,XOList):
    print("hey player",player)
    flag = 0
    while flag ==0:
        pos = int(input("Enter the position in between [0 to 8]"))
        if pos>=0 and pos<=8:
            if XOList[pos]==' ':
                print("valid input")
                if player == 0:
                    XOList[pos] = 'x'
                else:
                    XOList[pos] = 'o'
                return XOList
                flag=1
            else:
                print("please enter again,its occupied")
                flag=0
        else:
            print("please give valid input again")
            flag=0


# In[28]:


XO_list=takeInput(0,XO_list)


# In[31]:


XO_list=takeInput(0,XO_list)


# In[32]:


XO_list


# In[33]:


printBoard(XO_list)


# In[34]:


#if return is 0 then player A is winner
#if return is 1 then player B is winner
#if return is 2 then its a draw
def checkWin(XOlist):
    flag = 0
    for i in range(9):
        if XOlist[i] == ' ':
            flag = 1
        if flag == 0:
    if (XOlist[0] == 'o'and XOlist[1] == 'o'and XOlist[2] == 'o') or (XOlist[3] =='o'and XOlist[4] == 'o'and XOlist[5] == 'o') or (XOlist[6] == 'o'and XOlist[7] =='o'and XOlist[8] =='o') or (XOlist[0] == 'o'and XOlist[3] == 'o'and XOlist[6] == 'o') or (XOlist[1] == 'o'and XOlist[4] == 'o'and XOlist[7] == 'o') or (XOlist[2] == 'o'and XOlist[5] == 'o'and XOlist[8] == 'o') or (XOlist[0] == 'o'and XOlist[4] == 'o'and XOlist[8] == 'o') or (XOlist[6] == 'o'and XOlist[4] == 'o'and XOlist[2] == 'o'):
        print("player A is winner")
        return 0
    elif (XOlist[0] == 'x'and XOlist[1] == 'x'and XOlist[2] == 'x') or (XOlist[3] =='x'and XOlist[4] == 'x'and XOlist[5] == 'x') or (XOlist[6] == 'x'and XOlist[7] =='x'and XOlist[8] =='x') or (XOlist[0] == 'x'and XOlist[3] == 'x'and XOlist[6] == 'x') or (XOlist[1] == 'x'and XOlist[4] == 'x'and XOlist[7] == 'x') or (XOlist[2] == 'x'and XOlist[5] == 'x'and XOlist[8] == 'x') or (XOlist[0] == 'x'and XOlist[4] == 'x'and XOlist[8] == 'x') or (XOlist[6] == 'x'and XOlist[4] == 'x'and XOlist[2] == 'x'):
        print("player B is winner")
        return 1
    elif flag == 0:
        return 2
    else:
        return -1


# In[35]:


tmp = [0,1,2,3,4,5,6,7,8]
printBoard(tmp)


# In[36]:


printBoard(XO_list)


# In[37]:


checkWin(XO_list)


# In[ ]:


XO_list = emptyList_XO()
printBoard(XO_list)
play = whowillGoFirst()
gameStatus = -1
chance = 0
while gameStatus  == -1
    if play == 0:
        XO_list = takeInput(0,XO_list)
        gameStatus  = checkwin(XO_list)
        play = 1
    else:
        XO_list = takeInput(1,XO_list)
        gameStatus  = checkwin(XO_list)
        play = 0
    if gameStatus
    

