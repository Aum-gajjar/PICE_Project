from app.models import Product

from bs4 import BeautifulSoup
import requests

def productinfo(channel,valid_gtin_asin_list):

    if channel=="Amazon":

        cookies = {
            'session-id': '260-8610455-3934725',
            'i18n-prefs': 'INR',
            'ubid-acbin': '262-5000713-9388932',
            'lc-acbin': 'en_IN',
            'session-id-time': '2082787201l',
            'session-token': 'Uc/LW9wEtnJItNwBROD76KG4ROaPAHyYuOPO25WeYKAqf7LvYBEcEHy4KY+lqhk5zcb83i8vsqQaLJ8YoEY6ePYRuOyFK8lbUIV6PhqNaLsIQYyCE7fF57y0K1ymWaxENIaB7aiBwjyWnGnj0qwcG/0HAy/BvzTw2xnCQ+9NllqsWFZ7iBV4N09LhxbMMmKElwpmPLD2RrmE/Jbw3d14F/W3BLZMrrvwDBFuvl9WBKw=',
            'csm-hit': 'tb:3M3HYNZZV8J4H24R7N7K+s-3M3HYNZZV8J4H24R7N7K|1681277799674&t:1681277799674&adb:adblk_no',
        }

        headers = {
            'authority': 'www.amazon.in',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            # 'cookie': 'session-id=260-8610455-3934725; i18n-prefs=INR; ubid-acbin=262-5000713-9388932; lc-acbin=en_IN; session-id-time=2082787201l; session-token=Uc/LW9wEtnJItNwBROD76KG4ROaPAHyYuOPO25WeYKAqf7LvYBEcEHy4KY+lqhk5zcb83i8vsqQaLJ8YoEY6ePYRuOyFK8lbUIV6PhqNaLsIQYyCE7fF57y0K1ymWaxENIaB7aiBwjyWnGnj0qwcG/0HAy/BvzTw2xnCQ+9NllqsWFZ7iBV4N09LhxbMMmKElwpmPLD2RrmE/Jbw3d14F/W3BLZMrrvwDBFuvl9WBKw=; csm-hit=tb:3M3HYNZZV8J4H24R7N7K+s-3M3HYNZZV8J4H24R7N7K|1681277799674&t:1681277799674&adb:adblk_no',
            'device-memory': '8',
            'downlink': '2',
            'dpr': '1',
            'ect': '4g',
            'referer': 'https://www.amazon.in/s?k=B0BMGB2TPR',
            'rtt': '150',
            'sec-ch-device-memory': '8',
            'sec-ch-dpr': '1',
            'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-ch-viewport-width': '1366',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
            'viewport-width': '1366',
        }


        all_gtin_no = valid_gtin_asin_list

        for gtin_no in all_gtin_no:
            # print(gtin_no)
            input_params = gtin_no

            params = {
                'keywords': input_params,
                'qid': '1681274667',
                'sr': '8-1',
                'th': '1',
            }

            webpage = requests.get(
                'https://www.amazon.in/Samsung-Storage-MediaTek-Octa-core-Processor/dp/'+str(input_params)+'/ref=sr_1_1',
                params=params,
                cookies=cookies,
                headers=headers,
            )

            soup = BeautifulSoup(webpage.content, "lxml")
            title = soup.find("span",attrs={"id": 'productTitle'})
            title_value = title.string
            title_string = title_value.strip().replace(',', '')
            print("product Title = ", title_string)


            price = soup.find("span", attrs={'class': 'a-offscreen'}).string.strip().replace(',', '')
            # print("Products price = ", price)

            try:
                rating = soup.find("i", attrs={'class': 'a-icon a-icon-star a-star-4'}).string.strip().replace(',', '')

            except AttributeError:
                try:
                    rating = soup.find("span", attrs={'class': 'a-icon-alt'}).string.strip().replace(',', '')
                except:
                    rating = "NA"
            # print("Overall rating = ", rating)

            try:
                available = soup.find("div", attrs={'id': 'availability'})
                available = available.find("span", attrs={'class': 'a-size-medium a-color-success'}).string.strip().replace(',', '')

            except AttributeError:
                available = "NA"
            # print("Availability = ", available)

            product = Product(asingtin=gtin_no, title=title_string, price=price, rating=rating, stock=available)
            product.save()

    elif channel=="Snapdeal":

        cookies = {
            'SCOUTER': 'x3m50j8a53f74n',
            'versn': 'v1',
            'u': '168145408859312325',
            'sd.zone': 'NO_ZONE',
            'alps': 'akm',
            'isWebP': 'true',
            '_gcl_au': '1.1.489291664.1681454230',
            'st': 'utm_source%3Dadmitad_846%7Cutm_content%3Dadmitad_846%7Cutm_medium%3Dnull%7Cutm_campaign%3D64a9910bbfd90ffc533d94996200f3a9%7Cref%3Dnull%7Cutm_term%3Dnull%7Caff_id%3Dnull%7Caff_sub%3Dnull%7Caff_sub2%3Dnull%7C',
            'lt': 'utm_source%3Dadmitad_846%7Cutm_content%3Dadmitad_846%7Cutm_medium%3Dnull%7Cutm_campaign%3D64a9910bbfd90ffc533d94996200f3a9%7Cref%3Dnull%7Cutm_term%3Dnull%7Caff_id%3Dnull%7Caff_sub%3Dnull%7Caff_sub2%3Dnull%7C',
            'sdCPW': 'false',
            '_fbp': 'fb.1.1681454234430.1883527069',
            '__gads': 'ID=30f5e3c7e8c223a0:T=1681454254:S=ALNI_MbMPj-X_UO0sjyokBMz-RAKxfE41w',
            '__adroll_fpc': 'edb1337b2a5747507dce35f165a78b21-1681454257348',
            '__gpi': 'UID=00000bf4666dea2f:T=1681454254:RT=1681713373:S=ALNI_MYULxJeVW_B_ub6F8MAOCw-RVf32w',
            '__ar_v4': 'Z5YQR5LLINF2VIMT44RK3W%3A20230414%3A11%7CABU5CCWKZRGJVLAGFWVMWY%3A20230414%3A11%7CYEYVQC2UABBD3FDKIB2RYY%3A20230414%3A11',
            'JSESSIONID': '16EAC9AB9829925F9CE4549EE877A97D',
            'xg': '"eyJ3YXAiOnsiYWUiOiIxIn0sInBzIjp7ImF0IjoibyIsImNiIjoiQiJ9LCJzYyI6eyJzaGlwcGluZ19pbnRlcnZhbCI6ImxzdG1fMzEifSwidWlkIjp7Imd1aWQiOiJmM2NkZWIzMi03YjdlLTQwYTMtYTg5Yy1jYjFlYzAzNjk0MWYifX18fDE2ODE3MjQxNjg5MDk="',
            'xc': '"eyJ3YXAiOnsiYWUiOiIxIn0sInBzIjp7ImF0IjoibyIsImNiIjoiQiJ9LCJzYyI6eyJzaGlwcGluZ19pbnRlcnZhbCI6ImxzdG1fMzEifX0="',
            'vt': 'utm_source%3DDIRECT%7Cutm_content%3Dnull%7Cutm_medium%3Dnull%7Cutm_campaign%3Dnull%7Cref%3Dnull%7Cutm_term%3Dnull%7Caff_id%3Dnull%7Caff_sub%3Dnull%7Caff_sub2%3Dnull%7C',
            'lang': 'en',
            '_sdDPPageId': '1681722483892_3996_168145408859312325',
            '_uetsid': 'ab387c30dce911ed82f251e83c2574b8',
            '_uetvid': 'c8c57850da8e11ed90256f60d81c806d',
            's_pers': '%20s_vnum%3D1684046233433%2526vn%253D4%7C1684046233433%3B%20gpv_pn%3DhomePage%253Anew%7C1681724286274%3B%20s_invisit%3Dtrue%7C1681724286276%3B',
            'cto_bundle': '8LPtgl9MOWw3OHlwbkZPM1RhR1FjJTJCVXFPQVl5NU5VMXJvJTJGd1I2OVRXJTJGN3pYOWFISWpWSElxTXBPYUV5bXlFTWluUFhUVHZ0UWFVUjVPQzRNNG9tNlo4azQ3Y0xQSjVMbWxzR2FPRTJJRlZjeU1HTWglMkJYSkpZQ29aQWl4cjhrRWZZbHhDT2JKRzJPMmRJV3pqUk1XWlolMkJWVWRRJTNEJTNE',
            's_sess': '%20s_cc%3Dtrue%3B%20s_sq%3D%3B%20s_ppv%3D100%3B',
            'AWSALB': 'LcYWzJncGF2wjJLOAIOC3Xw812r4NHRBL+AyrGq3//GK0Ky8DmCsq1Wj+8JcDGasAHmsnbAdC6LXyIXfO12yw71mheHVpPSM+Ue79a1DzC/EEGKntdlXcIFKDD6G',
            'AWSALBCORS': 'LcYWzJncGF2wjJLOAIOC3Xw812r4NHRBL+AyrGq3//GK0Ky8DmCsq1Wj+8JcDGasAHmsnbAdC6LXyIXfO12yw71mheHVpPSM+Ue79a1DzC/EEGKntdlXcIFKDD6G',
            '_sdRefPgCookie': '%7B%22refPg%22%3A%22searchResult%22%2C%22refPgId%22%3A%221681714927244_522_168145408859312325%22%7D',
            '_sdRefEvtCookie': '%7B%22refEvt%22%3A%22eventLoggingLogging%22%2C%22refEvtId%22%3A%221681714928879_9239_168145408859312325%22%7D',
        }

        headers = {
            'authority': 'www.snapdeal.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            # 'cookie': 'SCOUTER=x3m50j8a53f74n; versn=v1; u=168145408859312325; sd.zone=NO_ZONE; alps=akm; isWebP=true; _gcl_au=1.1.489291664.1681454230; st=utm_source%3Dadmitad_846%7Cutm_content%3Dadmitad_846%7Cutm_medium%3Dnull%7Cutm_campaign%3D64a9910bbfd90ffc533d94996200f3a9%7Cref%3Dnull%7Cutm_term%3Dnull%7Caff_id%3Dnull%7Caff_sub%3Dnull%7Caff_sub2%3Dnull%7C; lt=utm_source%3Dadmitad_846%7Cutm_content%3Dadmitad_846%7Cutm_medium%3Dnull%7Cutm_campaign%3D64a9910bbfd90ffc533d94996200f3a9%7Cref%3Dnull%7Cutm_term%3Dnull%7Caff_id%3Dnull%7Caff_sub%3Dnull%7Caff_sub2%3Dnull%7C; sdCPW=false; _fbp=fb.1.1681454234430.1883527069; __gads=ID=30f5e3c7e8c223a0:T=1681454254:S=ALNI_MbMPj-X_UO0sjyokBMz-RAKxfE41w; __adroll_fpc=edb1337b2a5747507dce35f165a78b21-1681454257348; __gpi=UID=00000bf4666dea2f:T=1681454254:RT=1681713373:S=ALNI_MYULxJeVW_B_ub6F8MAOCw-RVf32w; __ar_v4=Z5YQR5LLINF2VIMT44RK3W%3A20230414%3A11%7CABU5CCWKZRGJVLAGFWVMWY%3A20230414%3A11%7CYEYVQC2UABBD3FDKIB2RYY%3A20230414%3A11; JSESSIONID=16EAC9AB9829925F9CE4549EE877A97D; xg="eyJ3YXAiOnsiYWUiOiIxIn0sInBzIjp7ImF0IjoibyIsImNiIjoiQiJ9LCJzYyI6eyJzaGlwcGluZ19pbnRlcnZhbCI6ImxzdG1fMzEifSwidWlkIjp7Imd1aWQiOiJmM2NkZWIzMi03YjdlLTQwYTMtYTg5Yy1jYjFlYzAzNjk0MWYifX18fDE2ODE3MjQxNjg5MDk="; xc="eyJ3YXAiOnsiYWUiOiIxIn0sInBzIjp7ImF0IjoibyIsImNiIjoiQiJ9LCJzYyI6eyJzaGlwcGluZ19pbnRlcnZhbCI6ImxzdG1fMzEifX0="; vt=utm_source%3DDIRECT%7Cutm_content%3Dnull%7Cutm_medium%3Dnull%7Cutm_campaign%3Dnull%7Cref%3Dnull%7Cutm_term%3Dnull%7Caff_id%3Dnull%7Caff_sub%3Dnull%7Caff_sub2%3Dnull%7C; lang=en; _sdDPPageId=1681722483892_3996_168145408859312325; _uetsid=ab387c30dce911ed82f251e83c2574b8; _uetvid=c8c57850da8e11ed90256f60d81c806d; s_pers=%20s_vnum%3D1684046233433%2526vn%253D4%7C1684046233433%3B%20gpv_pn%3DhomePage%253Anew%7C1681724286274%3B%20s_invisit%3Dtrue%7C1681724286276%3B; cto_bundle=8LPtgl9MOWw3OHlwbkZPM1RhR1FjJTJCVXFPQVl5NU5VMXJvJTJGd1I2OVRXJTJGN3pYOWFISWpWSElxTXBPYUV5bXlFTWluUFhUVHZ0UWFVUjVPQzRNNG9tNlo4azQ3Y0xQSjVMbWxzR2FPRTJJRlZjeU1HTWglMkJYSkpZQ29aQWl4cjhrRWZZbHhDT2JKRzJPMmRJV3pqUk1XWlolMkJWVWRRJTNEJTNE; s_sess=%20s_cc%3Dtrue%3B%20s_sq%3D%3B%20s_ppv%3D100%3B; AWSALB=LcYWzJncGF2wjJLOAIOC3Xw812r4NHRBL+AyrGq3//GK0Ky8DmCsq1Wj+8JcDGasAHmsnbAdC6LXyIXfO12yw71mheHVpPSM+Ue79a1DzC/EEGKntdlXcIFKDD6G; AWSALBCORS=LcYWzJncGF2wjJLOAIOC3Xw812r4NHRBL+AyrGq3//GK0Ky8DmCsq1Wj+8JcDGasAHmsnbAdC6LXyIXfO12yw71mheHVpPSM+Ue79a1DzC/EEGKntdlXcIFKDD6G; _sdRefPgCookie=%7B%22refPg%22%3A%22searchResult%22%2C%22refPgId%22%3A%221681714927244_522_168145408859312325%22%7D; _sdRefEvtCookie=%7B%22refEvt%22%3A%22eventLoggingLogging%22%2C%22refEvtId%22%3A%221681714928879_9239_168145408859312325%22%7D',
            'referer': 'https://www.snapdeal.com/product/veirdo-green-half-sleeve-tshirt/639827458615',
            'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        }

        all_snap_no = valid_gtin_asin_list
        for snap_no in all_snap_no:
            # print(snap_no)
            input_params = snap_no

            params = {
                'keyword': input_params,
                'santizedKeyword': '',
                'catId': '193',
                'categoryId': '0',
                'suggested': 'false',
                'vertical': '',
                'noOfResults': '20',
                'searchState': '',
                'clickSrc': 'go_header',
                'lastKeyword': '',
                'prodCatId': '',
                'changeBackToAll': 'false',
                'foundInAll': 'false',
                'categoryIdSearched': '',
                'cityPageUrl': '',
                'categoryUrl': '',
                'url': '',
                'utmContent': '',
                'dealDetail': '',
                'sort': 'rlvncy',
            }
            response = requests.get('https://www.snapdeal.com/search', params=params, cookies=cookies, headers=headers)

            soup = BeautifulSoup(response.content, "lxml")
            title = soup.find("p", attrs={'class': 'product-title'})
            title_value = title.string
            title_string = title_value.strip().replace(',', '')
            # print("product Title = ", title_string)

            try:
                price = soup.find("span", attrs={'class': 'lfloat product-price'}).string.strip().replace(',', '')

            except AttributeError:
                try:
                    price = soup.find("span", attrs={"id": 'display-price'}).string.strip().replace(',', '')
                except:
                    price = "NA"
            # print("Products price = ", price)

            try:
                rating = soup.find("p", attrs={'class': 'product-rating-count'}).string.strip().replace(',', '')

            except AttributeError:
                try:
                    rating = soup.find("span", attrs={'class': 'a-icon-alt'}).string.strip().replace(',', '')
                except:
                    rating = "NA"
            # print("Overall rating = ", rating)

            try:
                available = soup.find("div", attrs={'class': 'nudge-below-text'})
                available = available.find("span").string.strip().replace(',', '')

            except AttributeError:
                available = "NA"
            # print("Availability = ", available)

            product = Product(asingtin=snap_no, title=title_string, price=price, rating=rating, stock=available)
            product.save()

    elif channel == "Grainger":

        cookies = {
            'AB4': 'A',
            'DS2': 'B',
            's_ecid': 'MCMID%7C24073166837053943833318893866313890388',
            '__wwgmui': 'a3b5c9a2-9005-48a1-aad2-0deca38e0c0f',
            '_gcl_au': '1.1.922075115.1681735744',
            'Monetate': 'seg%3D1139434',
            'aam_uuid': '23816625796910475703344706505657963529',
            '_fbp': 'fb.1.1681735746445.113270248',
            'original_cart_id': '983950388',
            'btps': 'false',
            'sitetype': 'full',
            'AB1': 'G',
            'AB2': 'E',
            'AB5': 'A',
            'AB6': 'B',
            'AD1': 'B',
            'devPubRec': '1',
            'geo': '|AHMEDABAD|GJ|IN',
            'country': 'IN',
            'TLTSID': '25A7126E117C376BDF7168F7B853A457',
            'gws_lcp': '1',
            'full_gws_lcp': '1',
            'signin': 'A',
            'rmlPref': '1',
            'reg': 'A',
            'gws_pdp': '1',
            'ak_bmsc': 'B0AC214088120FA0EBC1B7B7A95ADBBB~000000000000000000000000000000~YAAQZzLUF4fbhACIAQAAIRwlAhMyWV7QYKLmLMHWKpFQRo2Z57C5TRRb/60VNDwcMDn76NhjrN7H7GVGNZVvbY1rvL/abRZGJeakl72+E0em6zwddWZJr9MFI/X14p97DRjE2qwqPWtrb5auQcen+xToHQJuXWm7BxHzt2ROnjei1dGXD1r+mzLPVyE0OceiYac+t0G6GrjQbsgf1mcSapisjyBxf6jKINbLIZb4iVg7kXNJhog37HgTUKfXPmsXz0SXSwXyIsnnJ06QvsgCPizM4QkuXezMcNG1iK2eruG4zjkr9emfwcXP9b4qMmn+xHLdxnDA/8SJYheYB+7LrwlYbhp8ADFwUpJaBHoJHd4bGw87a4Mr8jkP4SR51MpiufGmil0isOUKPr8=',
            'bm_sz': 'D862F996779AA9CE587FE692AD2ADF40~YAAQZzLUF4jbhACIAQAAIRwlAhO1wArvImdlg6g3lIkZFORzTfx3i6GiKHcj8CnCCKw+K72QkCu546DEO88cJqi9zv6p4N197zalpw3dw26RlHsYS7fDmi6At1L6cENhMdwySv/BYWR35HRwFXm539ebs7/vQ2BcJqHsQKkSSj2qwldLAE5i2shBDCLb53/VK7YpVH8azob/c0Qiv6dubD5u07aoHnbooNzkX/XCYsYd4evXO5lcRvRqOzyuVpxSEa1786jrHyMuR5PjaTdaf9eUR/ccsLek+C/RzV6MHjZciXtl8Q==~3227970~3618630',
            'PIM-SESSION-ID': 'JwsenG8ZFDOisXWh',
            'O': '2p',
            'AMCVS_FC80403D53C3ED6C0A490D4C%40AdobeOrg': '1',
            'AMCV_FC80403D53C3ED6C0A490D4C%40AdobeOrg': '1176715910%7CMCIDTS%7C19487%7CMCMID%7C24073166837053943833318893866313890388%7CMCAAMLH-1684267967%7C12%7CMCAAMB-1684267967%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1683670367s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.4.0',
            'JSESSIONID': '3709E6E1A9D1FBE68AD22814FC20CD29.96c6ea5c',
            'rxVisitor': '1683663167819R5TH95P77UNTGF87GI241A2USGO7UA35',
            'at_check': 'true',
            '_abck': 'F5DFC57B1704CAFEC45FF443BED13F3C~0~YAAQZzLUF5TbhACIAQAAvSMlAgkvL1oPYZztEKY80PZ3m+nbVUh0C+/4QxMv620+gOPS1H0CR0+v/kGaDI7XPXmIj3smhOyDE5Y4zuhQuE7NjcuCB8irLQK9hf0vcQEWkG03MtgOWBkDZz1lnU1WaCW6r7BjIejzF0w4jbyh1tadbouesuMDYUSWjD3qfWIRT/FA6j6snVpcQC09utN6Pv8higDcsS+gM5g8sh9Knfy6UPcftmWw9Ezw9UPZcsfi9e7TScNMmXyHmbRh8mx1xd3RXtgDGifO3Tbw6Sk06JssQd6iyF7JgSWMf0ZMACeYRVLqrm3SvRp8Jgx/J/ODpSQ7aYnpuAkN/T2ebcEcV3oJNAZXIsSR0CL+yDaHi3uPLuyjvetj4Zii5ggu56dBZGKVaIIO1B1+0E8=~-1~-1~1683666663',
            's_vnc30': '1686255169293%26vn%3D7',
            's_ivc': 'true',
            'ttc': '1683663169610',
            's_cc': 'true',
            '_gid': 'GA1.2.1892679794.1683663170',
            'ln_or': 'eyI0OTczMiI6ImQifQ%3D%3D',
            'isPickup': 'false',
            'dtCookie': 'v_4_srv_1_sn_ITT32URDMPMTL2L9848JPOSMTK4FJ1P8_app-3A51df13049352ae40_1_ol_0_perc_100000_mul_1_rcs-3Acss_0',
            'maId': '{"cid":"488893ffdd41294b04da74d98db2832d","sid":"5e543229-134b-47e5-a972-a933cbdc2bba","isSidSaved":true,"sessionStart":"2023-05-09T20:12:50.000Z"}',
            'CIP': '43.228.96.49',
            'dtLatC': '2',
            'OptanonConsent': 'isGpcEnabled=0&datestamp=Wed+May+10+2023+01%3A46%3A42+GMT%2B0530+(India+Standard+Time)&version=202211.2.0&isIABGlobal=false&hosts=&consentId=d072e280-0757-4453-b48b-0909859092c4&interactionCount=1&landingPath=NotLandingPage&groups=C0004%3A1%2CC0007%3A1%2CC0003%3A1%2CC0001%3A1%2CC0002%3A1&AwaitingReconsent=false',
            'gpv_v10': 'grainger%2Fproduct%2Flighting%2Fflashlights%2Fhandheld%20flashlights%2Ftactical%20handheld%20flashlights',
            's_sess': '%20hbx_lt%3D%3B',
            'gpv_c40': '404l39',
            '_tq_id.TV-7272906327-1.44e8': '9e005bd62167cc4b.1681735746.0.1683663403..',
            '_uetsid': 'df183e80eea511ed8d56b902eadb8b09',
            '_uetvid': '3bbff250dd1e11edb9c62d073e588316',
            '_ga': 'GA1.2.841398390.1681735744',
            'mbox': 'PC#3b41d67cf26d44378100a432d2f48f44.31_0#1746908202|session#b57a898fe87d43c4bd6f62a2eca97c25#1683665268',
            'bm_sv': '609BA4FB58FD21DD5B745D94B82A90B2~YAAQZzLUFzjvhACIAQAAtAMqAhNvLc0swWuI3EHDe+tgwcGfpK1g2KFAccXt6ftMZZxtwwuR7AYE8vl/qcr5i3dAC2pFn+7VpuNhth0pLvxgpK24ZmjoYKZVzeVMLogfSKV+FjnrYkwAeCi24qeE8pPXU+gc9801VyT2AEWcym4ClIT09+eL9n/pw52GlF9M1W0k7wWtNpm1lm5CoykCiKIgU7Fg+6vfy2iQHSG2tt9eTRgk2d/gmh2+T46C3FotdAvK~1',
            'dtPC': '1$63178415_104h-vAUFBFSOVRUKJAPEFRTIUUKRAULMFPECU-0e0',
            '_ga_94DBLXKMHK': 'GS1.1.1683663169.7.1.1683663505.59.0.0',
            's_nr30': '1683663525541-Repeat',
            'rxvt': '1683665371471|1683663167820',
        }

        headers = {
            'authority': 'www.grainger.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            # 'cookie': 'AB4=A; DS2=B; s_ecid=MCMID%7C24073166837053943833318893866313890388; __wwgmui=a3b5c9a2-9005-48a1-aad2-0deca38e0c0f; _gcl_au=1.1.922075115.1681735744; Monetate=seg%3D1139434; aam_uuid=23816625796910475703344706505657963529; _fbp=fb.1.1681735746445.113270248; original_cart_id=983950388; btps=false; sitetype=full; AB1=G; AB2=E; AB5=A; AB6=B; AD1=B; devPubRec=1; geo=|AHMEDABAD|GJ|IN; country=IN; TLTSID=25A7126E117C376BDF7168F7B853A457; gws_lcp=1; full_gws_lcp=1; signin=A; rmlPref=1; reg=A; gws_pdp=1; ak_bmsc=B0AC214088120FA0EBC1B7B7A95ADBBB~000000000000000000000000000000~YAAQZzLUF4fbhACIAQAAIRwlAhMyWV7QYKLmLMHWKpFQRo2Z57C5TRRb/60VNDwcMDn76NhjrN7H7GVGNZVvbY1rvL/abRZGJeakl72+E0em6zwddWZJr9MFI/X14p97DRjE2qwqPWtrb5auQcen+xToHQJuXWm7BxHzt2ROnjei1dGXD1r+mzLPVyE0OceiYac+t0G6GrjQbsgf1mcSapisjyBxf6jKINbLIZb4iVg7kXNJhog37HgTUKfXPmsXz0SXSwXyIsnnJ06QvsgCPizM4QkuXezMcNG1iK2eruG4zjkr9emfwcXP9b4qMmn+xHLdxnDA/8SJYheYB+7LrwlYbhp8ADFwUpJaBHoJHd4bGw87a4Mr8jkP4SR51MpiufGmil0isOUKPr8=; bm_sz=D862F996779AA9CE587FE692AD2ADF40~YAAQZzLUF4jbhACIAQAAIRwlAhO1wArvImdlg6g3lIkZFORzTfx3i6GiKHcj8CnCCKw+K72QkCu546DEO88cJqi9zv6p4N197zalpw3dw26RlHsYS7fDmi6At1L6cENhMdwySv/BYWR35HRwFXm539ebs7/vQ2BcJqHsQKkSSj2qwldLAE5i2shBDCLb53/VK7YpVH8azob/c0Qiv6dubD5u07aoHnbooNzkX/XCYsYd4evXO5lcRvRqOzyuVpxSEa1786jrHyMuR5PjaTdaf9eUR/ccsLek+C/RzV6MHjZciXtl8Q==~3227970~3618630; PIM-SESSION-ID=JwsenG8ZFDOisXWh; O=2p; AMCVS_FC80403D53C3ED6C0A490D4C%40AdobeOrg=1; AMCV_FC80403D53C3ED6C0A490D4C%40AdobeOrg=1176715910%7CMCIDTS%7C19487%7CMCMID%7C24073166837053943833318893866313890388%7CMCAAMLH-1684267967%7C12%7CMCAAMB-1684267967%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1683670367s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.4.0; JSESSIONID=3709E6E1A9D1FBE68AD22814FC20CD29.96c6ea5c; rxVisitor=1683663167819R5TH95P77UNTGF87GI241A2USGO7UA35; at_check=true; _abck=F5DFC57B1704CAFEC45FF443BED13F3C~0~YAAQZzLUF5TbhACIAQAAvSMlAgkvL1oPYZztEKY80PZ3m+nbVUh0C+/4QxMv620+gOPS1H0CR0+v/kGaDI7XPXmIj3smhOyDE5Y4zuhQuE7NjcuCB8irLQK9hf0vcQEWkG03MtgOWBkDZz1lnU1WaCW6r7BjIejzF0w4jbyh1tadbouesuMDYUSWjD3qfWIRT/FA6j6snVpcQC09utN6Pv8higDcsS+gM5g8sh9Knfy6UPcftmWw9Ezw9UPZcsfi9e7TScNMmXyHmbRh8mx1xd3RXtgDGifO3Tbw6Sk06JssQd6iyF7JgSWMf0ZMACeYRVLqrm3SvRp8Jgx/J/ODpSQ7aYnpuAkN/T2ebcEcV3oJNAZXIsSR0CL+yDaHi3uPLuyjvetj4Zii5ggu56dBZGKVaIIO1B1+0E8=~-1~-1~1683666663; s_vnc30=1686255169293%26vn%3D7; s_ivc=true; ttc=1683663169610; s_cc=true; _gid=GA1.2.1892679794.1683663170; ln_or=eyI0OTczMiI6ImQifQ%3D%3D; isPickup=false; dtCookie=v_4_srv_1_sn_ITT32URDMPMTL2L9848JPOSMTK4FJ1P8_app-3A51df13049352ae40_1_ol_0_perc_100000_mul_1_rcs-3Acss_0; maId={"cid":"488893ffdd41294b04da74d98db2832d","sid":"5e543229-134b-47e5-a972-a933cbdc2bba","isSidSaved":true,"sessionStart":"2023-05-09T20:12:50.000Z"}; CIP=43.228.96.49; dtLatC=2; OptanonConsent=isGpcEnabled=0&datestamp=Wed+May+10+2023+01%3A46%3A42+GMT%2B0530+(India+Standard+Time)&version=202211.2.0&isIABGlobal=false&hosts=&consentId=d072e280-0757-4453-b48b-0909859092c4&interactionCount=1&landingPath=NotLandingPage&groups=C0004%3A1%2CC0007%3A1%2CC0003%3A1%2CC0001%3A1%2CC0002%3A1&AwaitingReconsent=false; gpv_v10=grainger%2Fproduct%2Flighting%2Fflashlights%2Fhandheld%20flashlights%2Ftactical%20handheld%20flashlights; s_sess=%20hbx_lt%3D%3B; gpv_c40=404l39; _tq_id.TV-7272906327-1.44e8=9e005bd62167cc4b.1681735746.0.1683663403..; _uetsid=df183e80eea511ed8d56b902eadb8b09; _uetvid=3bbff250dd1e11edb9c62d073e588316; _ga=GA1.2.841398390.1681735744; mbox=PC#3b41d67cf26d44378100a432d2f48f44.31_0#1746908202|session#b57a898fe87d43c4bd6f62a2eca97c25#1683665268; bm_sv=609BA4FB58FD21DD5B745D94B82A90B2~YAAQZzLUFzjvhACIAQAAtAMqAhNvLc0swWuI3EHDe+tgwcGfpK1g2KFAccXt6ftMZZxtwwuR7AYE8vl/qcr5i3dAC2pFn+7VpuNhth0pLvxgpK24ZmjoYKZVzeVMLogfSKV+FjnrYkwAeCi24qeE8pPXU+gc9801VyT2AEWcym4ClIT09+eL9n/pw52GlF9M1W0k7wWtNpm1lm5CoykCiKIgU7Fg+6vfy2iQHSG2tt9eTRgk2d/gmh2+T46C3FotdAvK~1; dtPC=1$63178415_104h-vAUFBFSOVRUKJAPEFRTIUUKRAULMFPECU-0e0; _ga_94DBLXKMHK=GS1.1.1683663169.7.1.1683663505.59.0.0; s_nr30=1683663525541-Repeat; rxvt=1683665371471|1683663167820',
            'referer': 'https://www.grainger.com/product/BESSEY-Fixture-Clamp-4-1-4-in-Overall-44ZL27',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        }

        all_grainge_no = valid_gtin_asin_list
        for grainge_no in all_grainge_no:
            # print(grainge_no)
            input_params = grainge_no

            params = {
                'cpnuser': 'undefined',
                'searchBar': 'true',
                'searchQuery': input_params,
                'suggestConfigId': '1',
                'tier': 'Not Applicable',
            }
            response = requests.get(
                'https://www.grainger.com/product/DAYTON-Motor-Run-Capacitor-Round-' + str(input_params) + '',
                params=params,
                cookies=cookies,
                headers=headers,
            )

            soup = BeautifulSoup(response.content, "lxml")
            title = soup.find("h1", attrs={'class': 'lypQpT'})
            title_value = title.string
            title_string = title_value.strip().replace(',', '')
            # print("product Title = ", title_string)

            try:
                price = soup.find("span", attrs={'class': 'rbqU0E lVwVq5'}).string.strip().replace(',', '')

            except AttributeError:
                try:
                    price = soup.find("span", attrs={"id": 'pricing-component'}).string.strip().replace(',', '')
                except:
                    price = "NA"
            # print("Products price = ", price)

            try:
                rating = soup.find("p", attrs={'class': 'product-rating-count'}).string.strip().replace(',', '')

            except AttributeError:
                try:
                    rating = soup.find("span", attrs={'class': 'a-icon-alt'}).string.strip().replace(',', '')
                except:
                    rating = "NA"
            # print("Overall rating = ", rating)

            try:
                available = soup.find("div", attrs={'class': 'nudge-below-text'})
                available = available.find("span").string.strip().replace(',', '')

            except AttributeError:
                available = "NA"
            # print("Availability = ", available)

            product = Product(asingtin=grainge_no, title=title_string, price=price, rating=rating, stock=available)
            product.save()

    elif channel == "Zoro":
        cookies = {
            'ldId': '7b1d0470-c0d7-4124-973a-2850be7df25a',
            'zuid': 'XiJ4GjQ9Uh8Z29m1UfI4QbJp50aec00196b842595333f5ee51b38fc8a18171ba7d76a26fa7e43ddc92e190efd1f541431adb3a7c6865c0016b2a1445b3e3b1d7b40a5948d3b26656fe846cf620230419',
            'RES_TRACKINGID': 'b176badc-b6d0-4910-88d2-eae5e0567b39',
            'gbi_visitorId': 'clgnoggfs00013570gtzqrfv7',
            '_gcl_au': '1.1.1983911567.1681907765',
            '_fbp': 'fb.1.1681907764901.15971431',
            'cjConsent': 'MHxOfDB8Tnww',
            'cjUser': '9b3e7358-e534-45c5-aadd-2d951afb99a1',
            'cjCountry': 'IN',
            'FPID': 'FPID2.2.KHFezwKKhg59uqwd3hHQJ2MoreNznnaTBApixdJvO0U%3D.1681907765',
            '_svsid': '0c526f520e23898dd3f7aea9b6f60f0a',
            '_cs_c': '0',
            'interactionDetected': 'yes',
            '_pin_unauth': 'dWlkPU5XVTNZVFJsWlRFdE9EY3daUzAwWmpoaUxUa3dZMkl0TnpFME5tWTRPVFk1WXpOaA',
            'uid': '287d67f0-b771-4c5a-9b68-685a21491ec1',
            'utype': '',
            '__pr.11gr': 'nD8aYTtasg',
            'fs_uid': '#o-1HR607-na1#5534554959630336:6532754835230720:::#/1713443764',
            'sessionId': '7EPTKtZ4NP0Du4kRdcrQA1Jbab10750a2bdd8caed410406c91a4f425d10b0ac9a06484822ec3640092270dbc04a05e34b5fe8b72817dec682e436ca887a4a9f4843d47910a57b38ae556ffb720230509',
            '_abck': '78A3271E58D85E74C0A0522324435D63~0~YAAQxFI2F/JVkfqHAQAA0n0uAgkABXNRpFPq+Gy1zhNOeR07m/eZDsdood/FtJYWAcSrttglvBPgxW3/byuvxibimZfKMx0zrLRlEGx6WyVgcm3OSsSSzji4yMn7yvY1/wZZYJpo4kgwxCNAJB4opbbkv6s3VkI/AurmXyqBdcgG7zinx73vHICweNcqOsc9aHVQ0V54WRxWvybwsOMRbcXd7mDdQEgBO+YtzgTkbHzhg6Mrzkr3ucdDjjRuPNet2TfAm82z+G+zYO5yd4DzX0mU4aeY7406YWgQ0IwlZxBPgftftcNWfywHe74cGX+rKHiC38dAq8gdJTsgB4doyr2e99Lue38Aql03cnaPVuJvp6vhS5s35PuCRfsPMYBzV6ioNcOZ/DEhXLxUuxljavoKCmGJPQ==~-1~-1~-1',
            'bm_sz': '437D699433DA579027A35BAD61110381~YAAQxFI2F/VVkfqHAQAA0n0uAhN2MM9Na1i+Z02ACwImL/IhqMODQiwSFX6JZ9md9QcHkoqiv8y9A+I2fDySKiQ9Lb1Y7MDcjcJQJKHtGnwLI90xmuaK7hMDmBByLzdGyHEpAWOntITmtm/HiAuDPQvblUxfyht3ltDHVPG5K5ttxxdBloyDwwLVsK5xl0ZT2VefGZpwC3b9YFEWmLPU4x4tWrdlVGJKjKLT9wwg16zR2Ip4Q98I86tqzkUOwf41q5nq7VeJVAvjKBK2NjInDSVsYjg4zNY8AuL4CMyCzTgE~3747908~4534328',
            'cartLineItemCount': '0',
            'page_count': '16',
            '_cs_mk': '0.9748954904946643_1683663785035',
            'ak_bmsc': '0F51B86879B831635DE642327A2F8780~000000000000000000000000000000~YAAQxFI2F/dVkfqHAQAAJY0uAhP8IbjQ8qqBKtJoTpGktw2KzVcwqVbIAgF4l9kIQ1z1IMESsVdvEWuhl5zYzAnEZDKgiv2sWJZhRdIRe+ydIVQdhGtJ7RBKz2rc1mZEqGauH0WPBizTGrHDgb+cbHTs+w+0IjR/qcVEm3/HkYmc5RlCtAHGG7TpA0p71FZbXhYI1u1XO/98Fr/CPyPuc8BWpEoLQdsm/HoQr8JqMI6SWR6uS36bbFYQZ8XJbDYRAIhL6u12D+jXeIT233prI8GKQUa5eB9yGtyVPAqUVg95GTH+MWMee+qIk0RGgPcWiqjzk6ZIilPJGGRSMnMDeFyeXyfCgrNmuLVYuhK0E6NC/0vQoTZMT8JO8e2BJaSdKa7853hyTeOWKhi4+1hp5Jn7MZ9UFLcyU/fch1Zlesg5D2+BQ9fu+PEla74D+GCiMwUin2sHwCEzZ52OvK1SXQ5EvW13hTTKFoQKkYf8Ca0VJgcOGX8n',
            '_ga': 'GA1.2.492984694.1681907765',
            '_gid': 'GA1.2.629444741.1683663785',
            '_br_uid_2': 'uid%3D6945302739345%3Av%3D12.0%3Ats%3D1681907790173%3Ahc%3D16',
            'tfpsi': '068276ed-e69a-4c00-b6ac-de802d277619',
            'FPLC': 'FGVrvBP3upYlWv9zzLh4DIRTiO3u9SiB26JTK1eeltDb1BFIspwi2KAij0eqyu044RxbM3BDPxt9mvO7GPA1pIS7YIoQLjBWPcgcvM7kngnSOEvLSMLouGH1gkpgJg%3D%3D',
            'account-prompt': 'displayed',
            '_cs_cvars': '%7B%7D',
            'show-all-facets': '0',
            '_uetsid': '4ee925a0eea711edaacaef59d52855eb',
            '_uetvid': 'c1a22940deae11edb97663fe672500e6',
            '_ga_JM60PMS287': 'GS1.1.1683663785.8.1.1683663946.56.0.0',
            '_cs_id': 'daff5c4a-8a82-a91b-aa5f-edcbf2f82a3a.1681907767.8.1683663948.1683663786.1578495854.1716071767608',
            '_cs_s': '9.5.0.1683665748467',
            'bm_sv': '34CD1B9D2AC506611B3A68C2E7539694~YAAQvFI2F4MO7e+HAQAAOA0xAhPzykRgQtHvv+IkEWKsr+6HgG1hwb/sTvbjBuaNQ1kcB93OUKHhME4WuVUK+eNYIa00/Q9t7+gA1Pe3kEZtbNXlzknEtKNx7+gy/fBWAm4qDg7+wwOc9weRJczoQxptc4JfRMw1r4RRrR6B0i++5Ei3hMlaE4pwm4Tw6HcY2NUr+piHWKIdhHrNv3Cp5s4xdWkaxhVu9BRj7QXDe3RnOWDTWPK3Xbyaf0J01XU=~1',
            '_dd_s': 'logs=1&id=757ad02e-1630-4f5e-9f8c-23ff9f7d8955&created=1683663783469&expire=1683664899708&rum=0',
            'RT': '"z=1&dm=www.zoro.com&si=f8693bf4-6542-4ffb-8ba0-a942245aa457&ss=lhgpxxpy&sl=1&tt=6es&rl=1&ld=6eu&nu=labr5jyy&cl=3knp&ul=4y8k"',
        }

        headers = {
            'authority': 'www.zoro.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            # 'cookie': 'ldId=7b1d0470-c0d7-4124-973a-2850be7df25a; zuid=XiJ4GjQ9Uh8Z29m1UfI4QbJp50aec00196b842595333f5ee51b38fc8a18171ba7d76a26fa7e43ddc92e190efd1f541431adb3a7c6865c0016b2a1445b3e3b1d7b40a5948d3b26656fe846cf620230419; RES_TRACKINGID=b176badc-b6d0-4910-88d2-eae5e0567b39; gbi_visitorId=clgnoggfs00013570gtzqrfv7; _gcl_au=1.1.1983911567.1681907765; _fbp=fb.1.1681907764901.15971431; cjConsent=MHxOfDB8Tnww; cjUser=9b3e7358-e534-45c5-aadd-2d951afb99a1; cjCountry=IN; FPID=FPID2.2.KHFezwKKhg59uqwd3hHQJ2MoreNznnaTBApixdJvO0U%3D.1681907765; _svsid=0c526f520e23898dd3f7aea9b6f60f0a; _cs_c=0; interactionDetected=yes; _pin_unauth=dWlkPU5XVTNZVFJsWlRFdE9EY3daUzAwWmpoaUxUa3dZMkl0TnpFME5tWTRPVFk1WXpOaA; uid=287d67f0-b771-4c5a-9b68-685a21491ec1; utype=; __pr.11gr=nD8aYTtasg; fs_uid=#o-1HR607-na1#5534554959630336:6532754835230720:::#/1713443764; sessionId=7EPTKtZ4NP0Du4kRdcrQA1Jbab10750a2bdd8caed410406c91a4f425d10b0ac9a06484822ec3640092270dbc04a05e34b5fe8b72817dec682e436ca887a4a9f4843d47910a57b38ae556ffb720230509; _abck=78A3271E58D85E74C0A0522324435D63~0~YAAQxFI2F/JVkfqHAQAA0n0uAgkABXNRpFPq+Gy1zhNOeR07m/eZDsdood/FtJYWAcSrttglvBPgxW3/byuvxibimZfKMx0zrLRlEGx6WyVgcm3OSsSSzji4yMn7yvY1/wZZYJpo4kgwxCNAJB4opbbkv6s3VkI/AurmXyqBdcgG7zinx73vHICweNcqOsc9aHVQ0V54WRxWvybwsOMRbcXd7mDdQEgBO+YtzgTkbHzhg6Mrzkr3ucdDjjRuPNet2TfAm82z+G+zYO5yd4DzX0mU4aeY7406YWgQ0IwlZxBPgftftcNWfywHe74cGX+rKHiC38dAq8gdJTsgB4doyr2e99Lue38Aql03cnaPVuJvp6vhS5s35PuCRfsPMYBzV6ioNcOZ/DEhXLxUuxljavoKCmGJPQ==~-1~-1~-1; bm_sz=437D699433DA579027A35BAD61110381~YAAQxFI2F/VVkfqHAQAA0n0uAhN2MM9Na1i+Z02ACwImL/IhqMODQiwSFX6JZ9md9QcHkoqiv8y9A+I2fDySKiQ9Lb1Y7MDcjcJQJKHtGnwLI90xmuaK7hMDmBByLzdGyHEpAWOntITmtm/HiAuDPQvblUxfyht3ltDHVPG5K5ttxxdBloyDwwLVsK5xl0ZT2VefGZpwC3b9YFEWmLPU4x4tWrdlVGJKjKLT9wwg16zR2Ip4Q98I86tqzkUOwf41q5nq7VeJVAvjKBK2NjInDSVsYjg4zNY8AuL4CMyCzTgE~3747908~4534328; cartLineItemCount=0; page_count=16; _cs_mk=0.9748954904946643_1683663785035; ak_bmsc=0F51B86879B831635DE642327A2F8780~000000000000000000000000000000~YAAQxFI2F/dVkfqHAQAAJY0uAhP8IbjQ8qqBKtJoTpGktw2KzVcwqVbIAgF4l9kIQ1z1IMESsVdvEWuhl5zYzAnEZDKgiv2sWJZhRdIRe+ydIVQdhGtJ7RBKz2rc1mZEqGauH0WPBizTGrHDgb+cbHTs+w+0IjR/qcVEm3/HkYmc5RlCtAHGG7TpA0p71FZbXhYI1u1XO/98Fr/CPyPuc8BWpEoLQdsm/HoQr8JqMI6SWR6uS36bbFYQZ8XJbDYRAIhL6u12D+jXeIT233prI8GKQUa5eB9yGtyVPAqUVg95GTH+MWMee+qIk0RGgPcWiqjzk6ZIilPJGGRSMnMDeFyeXyfCgrNmuLVYuhK0E6NC/0vQoTZMT8JO8e2BJaSdKa7853hyTeOWKhi4+1hp5Jn7MZ9UFLcyU/fch1Zlesg5D2+BQ9fu+PEla74D+GCiMwUin2sHwCEzZ52OvK1SXQ5EvW13hTTKFoQKkYf8Ca0VJgcOGX8n; _ga=GA1.2.492984694.1681907765; _gid=GA1.2.629444741.1683663785; _br_uid_2=uid%3D6945302739345%3Av%3D12.0%3Ats%3D1681907790173%3Ahc%3D16; tfpsi=068276ed-e69a-4c00-b6ac-de802d277619; FPLC=FGVrvBP3upYlWv9zzLh4DIRTiO3u9SiB26JTK1eeltDb1BFIspwi2KAij0eqyu044RxbM3BDPxt9mvO7GPA1pIS7YIoQLjBWPcgcvM7kngnSOEvLSMLouGH1gkpgJg%3D%3D; account-prompt=displayed; _cs_cvars=%7B%7D; show-all-facets=0; _uetsid=4ee925a0eea711edaacaef59d52855eb; _uetvid=c1a22940deae11edb97663fe672500e6; _ga_JM60PMS287=GS1.1.1683663785.8.1.1683663946.56.0.0; _cs_id=daff5c4a-8a82-a91b-aa5f-edcbf2f82a3a.1681907767.8.1683663948.1683663786.1578495854.1716071767608; _cs_s=9.5.0.1683665748467; bm_sv=34CD1B9D2AC506611B3A68C2E7539694~YAAQvFI2F4MO7e+HAQAAOA0xAhPzykRgQtHvv+IkEWKsr+6HgG1hwb/sTvbjBuaNQ1kcB93OUKHhME4WuVUK+eNYIa00/Q9t7+gA1Pe3kEZtbNXlzknEtKNx7+gy/fBWAm4qDg7+wwOc9weRJczoQxptc4JfRMw1r4RRrR6B0i++5Ei3hMlaE4pwm4Tw6HcY2NUr+piHWKIdhHrNv3Cp5s4xdWkaxhVu9BRj7QXDe3RnOWDTWPK3Xbyaf0J01XU=~1; _dd_s=logs=1&id=757ad02e-1630-4f5e-9f8c-23ff9f7d8955&created=1683663783469&expire=1683664899708&rum=0; RT="z=1&dm=www.zoro.com&si=f8693bf4-6542-4ffb-8ba0-a942245aa457&ss=lhgpxxpy&sl=1&tt=6es&rl=1&ld=6eu&nu=labr5jyy&cl=3knp&ul=4y8k"',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        }

        all_zoro_no = valid_gtin_asin_list
        for zoro_no in all_zoro_no:
            # print(zoro_no)
            input_params = zoro_no

            params = {
                'recommended': 'true',
            }

            response = requests.get(
                'https://www.zoro.com/zoro-select-sealant-tape-12-x-520-in-21tf20/i/' + str(input_params) + '/',
                params=params,
                cookies=cookies,
                headers=headers,
            )

            soup = BeautifulSoup(response.content, "lxml")
            title = soup.find("h1", attrs={'class': 'text-h2'})
            title_value = title.string
            title_string = title_value.strip().replace(',', '')
            # print("Product Title = ", title_string)

            try:
                price = soup.find("div", attrs={'class': 'price font-weight-bold text-h2'}).string.strip().replace(',',
                                                                                                                   '')

            except AttributeError:
                try:
                    price = soup.find("span", attrs={"id": 'pricing-component'}).string.strip().replace(',', '')
                except:
                    price = "NA"
            # print("Products price = ", price)

            try:
                rating = soup.find("a", attrs={'class': 'long-review-count'}).string.strip().replace(',', '')

            except AttributeError:
                try:
                    rating = soup.find("div", attrs={'class': 'mr-2'}).string.strip().replace(',', '')
                except:
                    rating = "NA"
            # print("Overall rating = ", rating)

            try:
                available = soup.find("div", attrs={'class': 'badge-container'})
                available = available.find("span").string.strip().replace(',', '')

            except AttributeError:
                try:
                    available = soup.find("div", attrs={'class': 'avl-shipping-badge mb-2'}).string.strip().replace(',',
                                                                                                                    '')
                except:
                    available = "In Stock"
            # print("Availability = ", available)

            product = Product(asingtin=zoro_no, title=title_string, price=price, rating=rating, stock=available)
            product.save()

    elif channel == "HDSupply":
        cookies = {
            'WC_SESSION_ESTABLISHED': 'true',
            'WC_PERSISTENT': 'yKtVSY%2BL2FV92veKhQbCopiGvQh5sThNBastDuoGoCU%3D%3B2023-04-20+08%3A59%3A21.998_1681995561997-890973_10051',
            'WC_AUTHENTICATION_-1002': '-1002%2CygSxe4ygVZ3tvj5oSfCyG7ieocF%2BMnJJS8%2FwfxwFHxg%3D',
            'WC_ACTIVEPOINTER': '-1%2C10051',
            'WC_USERACTIVITY_-1002': '-1002%2C10051%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1163445765%2C7ka0EcERKh70VEh1%2BZvcmC9PLae6fNRZtBz7DwB1Kq6UeweclivUfvPWjXOhVKeSfXDFUqNueG27flIa6NXy52o0SLhVrCxN3WY%2BN2%2BZUNB1Ywpsr8VV2EB%2F%2FjCQSn4rPEnHEzCfJMCODztuVsLdU6B%2FWIfVWW8QfgZ%2F%2BOpHPWrdvGz8XZM88e4IyzFoEeS2uDcAloUafdGYaADjPoHFTja3kSa9hKpa9ZeqVaIQLdEFPy8YSPEjks1GKNOs6qlp',
            'WC_GENERIC_ACTIVITYDATA': '[2096538382%3Atrue%3Afalse%3A0%3AEt6hIwfv9MS%2FDywsYgOs6fiiW913mrBJKSbNYVPdhN0%3D][com.ibm.commerce.context.entitlement.EntitlementContext|10504%2610504%26null%26-2000%26null%26null%26null][com.ibm.commerce.context.audit.AuditContext|1681995561997-890973][com.ibm.commerce.context.globalization.GlobalizationContext|-1%26USD%26-1%26USD][com.ibm.commerce.store.facade.server.context.StoreGeoCodeContext|null%26null%26null%26null%26null%26null][com.ibm.commerce.catalog.businesscontext.CatalogContext|10054%26null%26false%26false%26false][com.ibm.commerce.context.experiment.ExperimentContext|null][com.ibm.commerce.context.ExternalCartContext|null][com.hds.commerce.marketing.businesscontext.PromotionContext|null][CTXSETNAME|Store][com.ibm.commerce.context.base.BaseContext|10051%26-1002%26-1002%26-1][com.ibm.commerce.giftcenter.context.GiftCenterContext|null%26null%26null]',
            'optimizelyEndUserId': 'oeu1681995564845r0.782673969202671',
            'at_check': 'true',
            'chevronExpanded': 'false',
            'AMCVS_907A67C25245B4980A490D4C%40AdobeOrg': '1',
            '_gcl_au': '1.1.1063420437.1681995565',
            's_ecid': 'MCMID%7C66214251764183316384195805197181773561',
            'ln_or': 'eyIxMTM3NjU4IjoiZCJ9',
            '_ga': 'GA1.2.485469987.1681995566',
            '_gid': 'GA1.2.762207137.1681995566',
            'cebs': '1',
            '_ce.clock_event': '1',
            '_ce.clock_data': '819%2C103.106.21.5%2C1',
            '_fbp': 'fb.1.1681995574244.324818016',
            'liveagent_oref': 'https://www.google.com/',
            '_mibhv': 'anon-1681995574459-2452903873_8072',
            's_cc': 'true',
            '_aeaid': '4baa159f-b234-434a-81ed-a090aa0495df',
            'liveagent_sid': '94336937-361a-4faf-9ded-0592a024e613',
            'liveagent_vc': '2',
            'liveagent_ptid': '94336937-361a-4faf-9ded-0592a024e613',
            'aelastsite': 'lghVfAfBCgL08EY2sizI3ytN6T8MF5zWqhG5MbMvpQUBaAsEZEE%2FM%2FEqAdQ7wt%2Bp',
            'aelreadersettings': '%7B%22c_big%22%3A0%2C%22rg%22%3A0%2C%22memph%22%3A0%2C%22contrast_setting%22%3A0%2C%22colorshift_setting%22%3A0%2C%22text_size_setting%22%3A0%2C%22space_setting%22%3A0%2C%22font_setting%22%3A0%2C%22k%22%3A0%2C%22k_disable_default%22%3A0%2C%22hlt%22%3A0%2C%22disable_animations%22%3A0%2C%22display_alt_desc%22%3A0%7D',
            'CompareItems_10051': '',
            'priceMode': '1',
            'QSI_SI_dnUk3cxyCVhxXHD_intercept': 'true',
            'searchTermHistory': '%7CBD-2100%7CBD-2100%7CBD-2100',
            'cto_bundle': 'szV2419PaWNOYUVwZWNZQkJVRHYlMkJ6a3FPdW5ra1lyazZHTUFtM2thaTdCMlBsazlsc0ZKU21rRWZMS3YlMkYlMkJJJTJGTEVBanpoSUklMkJOMklCRExXdjlVaWJ4eUR5JTJCM1RyZlFaR1psQWlTUDM0TEolMkZqUUNSVUNSVSUyRlhUQ0JLbXMxYngyemo0bFB2bVlPVG1sT2VrTFAxVWRNTTV6ZUFyMDV0SFYzbTJiWmRiSFFRRDVpdVNBJTNE',
            'fs_uid': '#GYHXA#6253320446136320:6163741863038976:::#/1713531565',
            's_prop51_s': 'Less%20than%201%20day',
            'JSESSIONID': '0000rVhIreqHlx8YfcdVIkpT7da:1f0h4pg9p',
            '__cf_bm': 'J9TRmVKTPLXlFXvbrnMTUdMDfbgh7z3KUjyI2Hfd0M0-1682052969-0-AZKzzH/WQ6iY4Bja+3A2ErSwoNunTV32ktMjPbg5v24bt3qhz9x34ICBQqD42gIwMboCs/+jpZsrswUhMr6rqomLTFc6U6NREV1dWOn0Zf6Ruf2JpQI0F1r1mmcjtPVKAwUtLhRwsIlBojuJbUK9b3Q=',
            'currentSDID': '3058C50A55B2B705-19C5DD0801B04E13',
            'cebsp_': '14',
            '_ce.s': 'v~02bcca565f450b30d1fd88cd6f9a9cdbf501dcc0~vpv~0~v11.rlc~1682052970703~ir~1~gtrk.la~lgp4qsi0',
            '_uetsid': '2f188aa0df7b11ed8f964923d00e593f',
            '_uetvid': '2f189540df7b11ed82ce37dde6dffe8a',
            '_br_uid_2': 'uid%3D135874164489%3Av%3D12.0%3Ats%3D1681995575611%3Ahc%3D14',
            'prevPage': 'homepage',
            'mbox': 'PC#23a0d75c01994b58bc565b97b572420d.31_0#1745297769|session#5f2b9fe2963442bebb739eaa20542d8d#1682054834',
            'AMCV_907A67C25245B4980A490D4C%40AdobeOrg': '1176715910%7CMCIDTS%7C19468%7CMCMID%7C66214251764183316384195805197181773561%7CMCAAMLH-1682657774%7C12%7CMCAAMB-1682657774%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1682060174s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.4.0',
            'aeatstartmessage': 'true',
            's_nr': '1682053178413-Repeat',
            '1yrNewRepeat': '1682053178413-Repeat',
            's_prop51': '1682053178414',
            's_sq': '%5B%5BB%5D%5D',
        }

        headers = {
            'authority': 'hdsupplysolutions.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            # 'cookie': 'WC_SESSION_ESTABLISHED=true; WC_PERSISTENT=yKtVSY%2BL2FV92veKhQbCopiGvQh5sThNBastDuoGoCU%3D%3B2023-04-20+08%3A59%3A21.998_1681995561997-890973_10051; WC_AUTHENTICATION_-1002=-1002%2CygSxe4ygVZ3tvj5oSfCyG7ieocF%2BMnJJS8%2FwfxwFHxg%3D; WC_ACTIVEPOINTER=-1%2C10051; WC_USERACTIVITY_-1002=-1002%2C10051%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1163445765%2C7ka0EcERKh70VEh1%2BZvcmC9PLae6fNRZtBz7DwB1Kq6UeweclivUfvPWjXOhVKeSfXDFUqNueG27flIa6NXy52o0SLhVrCxN3WY%2BN2%2BZUNB1Ywpsr8VV2EB%2F%2FjCQSn4rPEnHEzCfJMCODztuVsLdU6B%2FWIfVWW8QfgZ%2F%2BOpHPWrdvGz8XZM88e4IyzFoEeS2uDcAloUafdGYaADjPoHFTja3kSa9hKpa9ZeqVaIQLdEFPy8YSPEjks1GKNOs6qlp; WC_GENERIC_ACTIVITYDATA=[2096538382%3Atrue%3Afalse%3A0%3AEt6hIwfv9MS%2FDywsYgOs6fiiW913mrBJKSbNYVPdhN0%3D][com.ibm.commerce.context.entitlement.EntitlementContext|10504%2610504%26null%26-2000%26null%26null%26null][com.ibm.commerce.context.audit.AuditContext|1681995561997-890973][com.ibm.commerce.context.globalization.GlobalizationContext|-1%26USD%26-1%26USD][com.ibm.commerce.store.facade.server.context.StoreGeoCodeContext|null%26null%26null%26null%26null%26null][com.ibm.commerce.catalog.businesscontext.CatalogContext|10054%26null%26false%26false%26false][com.ibm.commerce.context.experiment.ExperimentContext|null][com.ibm.commerce.context.ExternalCartContext|null][com.hds.commerce.marketing.businesscontext.PromotionContext|null][CTXSETNAME|Store][com.ibm.commerce.context.base.BaseContext|10051%26-1002%26-1002%26-1][com.ibm.commerce.giftcenter.context.GiftCenterContext|null%26null%26null]; optimizelyEndUserId=oeu1681995564845r0.782673969202671; at_check=true; chevronExpanded=false; AMCVS_907A67C25245B4980A490D4C%40AdobeOrg=1; gcl_au=1.1.1063420437.1681995565; s_ecid=MCMID%7C66214251764183316384195805197181773561; ln_or=eyIxMTM3NjU4IjoiZCJ9; ga=GA1.2.485469987.1681995566; gid=GA1.2.762207137.1681995566; cebs=1; ce.clock_event=1; ce.clock_data=819%2C103.106.21.5%2C1; fbp=fb.1.1681995574244.324818016; liveagent_oref=https://www.google.com/; mibhv=anon-1681995574459-2452903873_8072; s_cc=true; aeaid=4baa159f-b234-434a-81ed-a090aa0495df; liveagent_sid=94336937-361a-4faf-9ded-0592a024e613; liveagent_vc=2; liveagent_ptid=94336937-361a-4faf-9ded-0592a024e613; aelastsite=lghVfAfBCgL08EY2sizI3ytN6T8MF5zWqhG5MbMvpQUBaAsEZEE%2FM%2FEqAdQ7wt%2Bp; aelreadersettings=%7B%22c_big%22%3A0%2C%22rg%22%3A0%2C%22memph%22%3A0%2C%22contrast_setting%22%3A0%2C%22colorshift_setting%22%3A0%2C%22text_size_setting%22%3A0%2C%22space_setting%22%3A0%2C%22font_setting%22%3A0%2C%22k%22%3A0%2C%22k_disable_default%22%3A0%2C%22hlt%22%3A0%2C%22disable_animations%22%3A0%2C%22display_alt_desc%22%3A0%7D; CompareItems_10051=; priceMode=1; QSI_SI_dnUk3cxyCVhxXHD_intercept=true; searchTermHistory=%7CBD-2100%7CBD-2100%7CBD-2100; cto_bundle=szV2419PaWNOYUVwZWNZQkJVRHYlMkJ6a3FPdW5ra1lyazZHTUFtM2thaTdCMlBsazlsc0ZKU21rRWZMS3YlMkYlMkJJJTJGTEVBanpoSUklMkJOMklCRExXdjlVaWJ4eUR5JTJCM1RyZlFaR1psQWlTUDM0TEolMkZqUUNSVUNSVSUyRlhUQ0JLbXMxYngyemo0bFB2bVlPVG1sT2VrTFAxVWRNTTV6ZUFyMDV0SFYzbTJiWmRiSFFRRDVpdVNBJTNE; fs_uid=#GYHXA#6253320446136320:6163741863038976:::#/1713531565; s_prop51_s=Less%20than%201%20day; JSESSIONID=0000rVhIreqHlx8YfcdVIkpT7da:1f0h4pg9p; _cf_bm=J9TRmVKTPLXlFXvbrnMTUdMDfbgh7z3KUjyI2Hfd0M0-1682052969-0-AZKzzH/WQ6iY4Bja+3A2ErSwoNunTV32ktMjPbg5v24bt3qhz9x34ICBQqD42gIwMboCs/+jpZsrswUhMr6rqomLTFc6U6NREV1dWOn0Zf6Ruf2JpQI0F1r1mmcjtPVKAwUtLhRwsIlBojuJbUK9b3Q=; currentSDID=3058C50A55B2B705-19C5DD0801B04E13; cebsp_=14; ce.s=v~02bcca565f450b30d1fd88cd6f9a9cdbf501dcc0~vpv~0~v11.rlc~1682052970703~ir~1~gtrk.la~lgp4qsi0; uetsid=2f188aa0df7b11ed8f964923d00e593f; uetvid=2f189540df7b11ed82ce37dde6dffe8a; _br_uid_2=uid%3D135874164489%3Av%3D12.0%3Ats%3D1681995575611%3Ahc%3D14; prevPage=homepage; mbox=PC#23a0d75c01994b58bc565b97b572420d.31_0#1745297769|session#5f2b9fe2963442bebb739eaa20542d8d#1682054834; AMCV_907A67C25245B4980A490D4C%40AdobeOrg=1176715910%7CMCIDTS%7C19468%7CMCMID%7C66214251764183316384195805197181773561%7CMCAAMLH-1682657774%7C12%7CMCAAMB-1682657774%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1682060174s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.4.0; aeatstartmessage=true; s_nr=1682053178413-Repeat; 1yrNewRepeat=1682053178413-Repeat; s_prop51=1682053178414; s_sq=%5B%5BB%5D%5D',
            'referer': 'https://hdsupplysolutions.com/',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        }

        all_hd_no = valid_gtin_asin_list
        for hd_no in all_hd_no:
            print(hd_no)
            input_params = hd_no

            params = {
                'categoryId': '',
                'storeId': '10051',
                'catalogId': '10054',
                'langId': '-1',
                'sType': 'SimpleSearch',
                'resultCatEntryType': '2',
                'showResultsPage': 'true',
                'searchSource': 'Q',
                'pageView': 'grid',
                'beginIndex': '0',
                'pageSize': '24',
                'searchTerm': input_params,  # Change searchTerm to get diffrent results
            }

            response = requests.get('https://hdsupplysolutions.com/SearchDisplay', params=params, cookies=cookies,
                                    headers=headers)

            soup = BeautifulSoup(response.content, "lxml")
            try:
                title = soup.find("div", attrs={'class': 'type--body-medium'}).string.strip().replace(',', '')

            except AttributeError:
                try:
                    title = soup.find("h1", attrs={
                        "class": 'font-weight-bolder feco-seo-title ecom-proddetail-title'}).string.strip().replace(',',
                                                                                                                    '')
                except AttributeError:
                    try:
                        title = soup.find("span").string.strip().replace(',', '')
                    except:
                        title = "NA"
            # print("Product = ", title)
            try:
                price = soup.find("span",
                                  attrs={'class': 'type--body-x-large price--offerprice'}).string.strip().replace(',',
                                                                                                                  '')

            except AttributeError:
                try:
                    price = soup.find("span", attrs={"id": 'font-weight-600'}).string.strip().replace(',', '')
                except:
                    price = "NA"
            # print("Products price = ", price)

            try:
                rating = soup.find("p", attrs={'class': 'product-rating-count'}).string.strip().replace(',', '')

            except AttributeError:
                try:
                    rating = soup.find("span", attrs={'class': 'a-icon-alt'}).string.strip().replace(',', '')
                except:
                    rating = "NA"
            # print("Overall rating = ", rating)

            try:
                available = soup.find("div", attrs={'class': 'nudge-below-text'})
                available = available.find("span").string.strip().replace(',', '')

            except AttributeError:
                available = "NA"
            # print("Availability = ", available)

            product = Product(asingtin=hd_no, title=title, price=price, rating=rating, stock=available)
            product.save()
