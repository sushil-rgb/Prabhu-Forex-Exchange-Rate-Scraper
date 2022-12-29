import random
from bs4 import BeautifulSoup
from lxml import etree


def userAgents():
    with open('user-agents.txt') as f:
        agents = f.read().split("\n")
    return random.choice(agents)


class PrabhuForex:
    def __init__(self, play):
        print(f"Initiating the automation. Powered by Playwright.")
        prabhuUrl = "https://www.prabhubank.com/forex"
        self.browser = play.chromium.launch(headless=True, slow_mo=1*1000)
        self.page = self.browser.new_page(user_agent=userAgents())    
        self.page.goto(prabhuUrl)
        self.page.wait_for_url(prabhuUrl, timeout=30*100) 
        try:
            content = self.page.content()
            self.soup = BeautifulSoup(content, 'lxml')
            # Below index is the number of column available in the forex table:
            self.exchange_rate = [currency.find_all('td')[2].text.strip() for currency in self.soup.find('tbody', id='table_body').find_all('tr')]
                                                        # Default value is 2:> Buying(Notes of below Deno 50)
                                                        # 0: selects Currency,
                                                        # 1 :> Unit,
                                                        # 2: Buying(Notes of below Deno 50),
                                                        # 3:> Buying(Notes of Deno 50 and above),
                                                        # 4:>(Selling/Rs),   
                                                        # Selecting below 0 and beyond 4 will throw an error.                                                     
        except Exception as e:
            print(f"Oops! Content loading error. Please try again in few minutes | {e}")
        self.browser.close()

    def latest_date(self):
        # Using lxml to select xpath selectors via beautifulsoup
        dom = etree.HTML(str(self.soup))
        date = ''.join([d.get('value') for d in dom.xpath("//input[@name='forexFilter']")])        
        return date
    
    def usDollar(self):
        usDollarValue = self.exchange_rate[0]
        return float(usDollarValue)
    
    def euro(self):
        euroValue = self.exchange_rate[1]
        return float(euroValue)
    
    def poundSterling(self):
        poundSterlingValue = self.exchange_rate[2]
        return float(poundSterlingValue)
    
    def australianDollar(self):
        australianDollarValue = self.exchange_rate[3]
        return float(australianDollarValue)
    
    def swissFrank(self):
        swissFrankValue = self.exchange_rate[4]
        return float(swissFrankValue)
    
    def canadianDollar(self):
        canadianDollarValue = self.exchange_rate[5]
        return float(canadianDollarValue)
    
    def singaporeDollar(self):
        singaporeValue = self.exchange_rate[6]
        return float(singaporeValue)
    
    def japaneseYen(self):
        japaneseYenValue = self.exchange_rate[7]
        return float(japaneseYenValue)
    
    def chineseYuan(self):
        chineseYuanValue = self.exchange_rate[8]
        return float(chineseYuanValue)
    
    def qatariRiyal(self):
        qatariRiyalValue = self.exchange_rate[9]
        return float(qatariRiyalValue)
    
    def saudiRiyal(self):
        saudiRiyalValue = self.exchange_rate[10]
        return float(saudiRiyalValue)
    
    def thaiBhat(self):
        thaiBhatValue = self.exchange_rate[11]
        return float(thaiBhatValue)
    
    def malaysianRinggit(self):
        malaysianRinggitValue = self.exchange_rate[12]
        return float(malaysianRinggitValue)
    
    def uaeDirham(self):
        uaeDirhamValue = self.exchange_rate[13]
        return float(uaeDirhamValue)
    
    def hongkongDollar(self):
        hongkongDollarValue = self.exchange_rate[14]
        return float(hongkongDollarValue)
    
    def danishKroner(self):
        danishKronerValue = self.exchange_rate[15]
        return float(danishKronerValue)
    
    def swedishKroner(self):
        swedishKronerValue = self.exchange_rate[16]
        return float(swedishKronerValue)
    
    def southKoreanWon(self):
        southKoreanValue = self.exchange_rate[17]
        return float(southKoreanValue)
    
    def indianRupees(self):
        indianRupeesValue = self.exchange_rate[18]
        return float(indianRupeesValue)
    
    def bahrainDinar(self):
        bahrainDinarValue = self.exchange_rate[19]
        return float(bahrainDinarValue)
    
    def kuwaitiDinar(self):
        kuwaitiDinarValue = self.exchange_rate[20]
        return float(kuwaitiDinarValue)

    