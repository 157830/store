import streamlit as st
import requests

def getAllBookstore() -> list:
    url = "https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    res = response.json()
    return res

def getCountyOption(items) ->list:
    optionList = []
    for item in items:
        name = item['cityName'][0:3]
        if name not in optionList:
            optionList.append(name)
    return optionList

def getDistrictOption(items, target) ->list:
    optionList = []
    for item in items:
        name = item['cityName']
        if target not in name: continue
        name.strip()
        district = name[5:]
        if len(district) == 0: continue
        if district not in optionList:
            optionList.append(district)
    return optionList

def getSpecificBookstore(items, county, districts):
    specificBookstoreList = []
    for item in items:
        name = item['cityName']
        if county not in name: continue
        for district in districts:
            if district not in name: continue
            specificBookstoreList.append(item)
    return specificBookstoreList

def getBookstoreInfo(items):
    expanderList = []
    for item in items:
        expander = st.expander(item['name'])
        expander.image(item['representImage'])
        expander.metric('hitRate', item['hitRate'])
        expander.subheader('Introduction')
        expander.write(item['intro'])
        expander.subheader('Address')
        expander.write(item['address'])
        expander.subheader('Open Time')
        expander.write(item['openTime'])
        expander.subheader('Email')
        expander.write(item['email'])
        expanderList.append(expander)
    return expanderList

def app():
    bookstoreList = getAllBookstore()

    countyOption = getCountyOption(bookstoreList)

    st.header('特色書店地圖')
    st.metric('Total bookstore', len(bookstoreList))
    county = st.selectbox('請選擇縣市', countyOption)
    districtOption = getDistrictOption(bookstoreList, county)
    district = st.multiselect('請選擇區域', districtOption)

    specificBookstore = getSpecificBookstore(bookstoreList, county, district)
    num = len(specificBookstore)
    st.write(f'總共有{num}項結果', num)

    specificBookstore.sort(key = lambda item: item['hitRate'], reverse=True)
    bookstoreInfo = getBookstoreInfo(specificBookstore)

if __name__ == '__main__':
    app()
    def getSpecificBookstore(items, county):
    specificBookstoreList = []
    for item in items:
	name = item['cityName']


	return specificBookstoreList

def app():
	bookstoreList = getAllBookstore()

	countyOption = getCountyOption(bookstoreList)
	
	st.header('特色書店地圖')
	st.metric('Total bookstore', len(bookstoreList))
	county = st.selectbox('請選擇縣市', countyOption) 
	#districtOption = getDistrictOption(bookstoreList, county)
	#district = st.multiselect('請選擇區域', districtOption) 
	
	# 呼叫 getSpecificBookstore 並將回傳值賦值給變數 specificBookstore
	num = len(specificBookstore)
	# 用 st.write 將目標書店的總數量計算出來，格式：總共有3項結果
    def getBookstoreInfo(items):
	expanderList = []
    for item in items 
        expander = st.expander(item['name'])
        expander.image(item['representImage'])
        expander.metric('hitRate', item['hitRate'])
        expander.subheader('Introduction')
        # 用 expander.write 呈現書店的 Introduction
        expander.subheader('Address')
        # 用 expander.write 呈現書店的 Address
        expander.subheader('Open Time')
        # 用 expander.write 呈現書店的 Open Time
	expander.subheader('Email')
	# 用 expander.write 呈現書店的 Email
        # 將該 expander 放到 expanderList 中
 return expanderList
