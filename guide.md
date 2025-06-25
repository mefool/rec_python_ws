
# Setup and Tests for REC Document Automatic Fill

## 1. Virtual Enviroment
``` shell
dir c:\python_api_dotnet #should rename to a better name
mkdir venv
python -m venv .\venv\

# Activate 
# .\venv\Scripts\activate.bat #Linux
.\venv\Scripts\activate.bat # Windows CMD
.\venv\Scripts\Activate.ps1 # Windows Powershell
# if "Activate.ps1 cannot be loaded because running scripts is disabled on this system."
# > Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

# PowerShell should now show when running "pip list"
(venv) PS C:\python_api_to_dotnet> pip list
Package Version
------- -------
pip     25.0.1
```
###

``` powershell
(venv) PS C:\python_api_to_dotnet> Get-Command python 

CommandType   Name         Version    Source
-----------   ----         -------    ------
Application   python.exe   3.13.31... C:\python_api_to_dotnet\venv\Scripts\python.exe
```

### 1.1. Extra Validation
`dir /s "python_api_to_dotnet" `
Total Files Listed: `872 File(s)     12 823 065 bytes`


## 2. Required Packages
### 2.1 fastapi
``` powershell
(venv) PS C:\python_api_to_dotnet> pip install "fastapi[standard]"
```
#### 2.1.1 Extra Validation
`dir /s "python_api_to_dotnet" `
``` shell
Total Files Listed:                                                                                                            3512 File(s)     48 957 195 bytes
```
`python.exe -m pip install --upgrade pip`


### 2.2 pypdfform
`(venv) PS C:\python_api_to_dotnet> pip install PyPDFForm`
> `Successfully installed PyPDFForm-2.3.3 cffi-1.17.1 chardet-5.2.0 cryptography-44.0.3 pillow-11.2.1 pycparser-2.22 pypdf-5.5.0 reportlab-4.4.0`
#### 2.2.1 Extra
```
     Total Files Listed:
     4640 File(s)     82 067 390 bytes
```
### 2.3 pip list
```
(venv) PS C:\python_api_to_dotnet> pip list
Package           Version
----------------- ---------
annotated-types   0.7.0
anyio             4.9.0
certifi           2025.4.26
cffi              1.17.1
chardet           5.2.0
click             8.2.0
colorama          0.4.6
cryptography      44.0.3
dnspython         2.7.0
email_validator   2.2.0
fastapi           0.115.12
fastapi-cli       0.0.7
h11               0.16.0
httpcore          1.0.9
httptools         0.6.4
httpx             0.28.1
idna              3.10
Jinja2            3.1.6
markdown-it-py    3.0.0
MarkupSafe        3.0.2
mdurl             0.1.2
pillow            11.2.1
pip               25.1.1
pycparser         2.22
pydantic          2.11.4
pydantic_core     2.33.2
Pygments          2.19.1
pypdf             5.5.0
PyPDFForm         2.3.3
python-dotenv     1.1.0
python-multipart  0.0.20
PyYAML            6.0.2
reportlab         4.4.0
rich              14.0.0
rich-toolkit      0.14.6
shellingham       1.5.4
sniffio           1.3.1
starlette         0.46.2
typer             0.15.3
typing_extensions 4.13.2
typing-inspection 0.4.0
uvicorn           0.34.2
watchfiles        1.0.5
websockets        15.0.1
	```

#### 2.3 pip freeze
```
(venv) PS C:\python_api_to_dotnet> pip freeze
annotated-types==0.7.0
anyio==4.9.0
certifi==2025.4.26
cffi==1.17.1
chardet==5.2.0
click==8.2.0
colorama==0.4.6
cryptography==44.0.3
dnspython==2.7.0
email_validator==2.2.0
fastapi==0.115.12
fastapi-cli==0.0.7
h11==0.16.0
httpcore==1.0.9
httptools==0.6.4
httpx==0.28.1
idna==3.10
Jinja2==3.1.6
markdown-it-py==3.0.0
MarkupSafe==3.0.2
mdurl==0.1.2
pillow==11.2.1
pycparser==2.22
pydantic==2.11.4
pydantic_core==2.33.2
Pygments==2.19.1
pypdf==5.5.0
PyPDFForm==2.3.3
python-dotenv==1.1.0
python-multipart==0.0.20
PyYAML==6.0.2
reportlab==4.4.0
rich==14.0.0
rich-toolkit==0.14.6
shellingham==1.5.4
sniffio==1.3.1
starlette==0.46.2
typer==0.15.3
typing-inspection==0.4.0
typing_extensions==4.13.2
uvicorn==0.34.2
watchfiles==1.0.5
websockets==15.0.1
```



## 3. Running
### 3.1 python server (VSCode command line)
`(venv) PS C:\python_api_to_dotnet> fastapi dev main.py`
``` shell
   FastAPI   Starting development server 🚀

             Searching for package file structure from directories with __init__.py files
             Importing from C:\python_api_to_dotnet
 
    module   🐍 main.py

      code   Importing the FastAPI app object from the module with the following code:

             from main import app

       app   Using import string: main:app

    server   Server started at http://127.0.0.1:8000
    server   Documentation at http://127.0.0.1:8000/docs

       tip   Running in development mode, for production use: fastapi run

             Logs:

      INFO   Will watch for changes in these directories: ['C:\\python_api_to_dotnet']
      INFO   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
      INFO   Started reloader process [33448] using WatchFiles
      INFO   Started server process [23640]
      INFO   Waiting for application startup.
      INFO   Application startup complete.
```
### 3.2 Chrome Client
#### http://127.0.0.1:8000
`{"root":"Hello World"}`
##### http://127.0.0.1:8000/rec_template
(EECS-GO-Standard-contract_V2.2.pdf download)
##### http://127.0.0.1:8000/rec_example
(pdf download)
##### http://127.0.0.1:8000/rec_complete
`{"detail":"Method Not Allowed"}`

### 3.2 Chrome Client (Boomerang Extension)
PUT Request
http://127.0.0.1:8000/rec_complete
#### 3.2.1 (Body)
``` json
{
  "currency": "EURO",
"group1_int": "0",
"group2_int": "1",
"tk_272": "total_contract_price",
"tk_273": "total_quantity",
"tk_336": "table_02F",
"tk_337": "table_02E",
"tk_338": "table_02D",
"tk_339": "table_02C",
"tk_340": "table_02B",
"tk_341": "table_02A",
"tk_342": "table_01F_contract_price",
"tk_343": "table_01E_certif_price",
"tk_344": "table_01D_quantity",
"tk_345": "table_01C_deliverydate",
"tk_346": "table_01B_tech",
"tk_347": "table_01A_prod_period",
"tk_367": "special_conditions",
"tk_370": "governing_law_accordance",
"tk_437": "seller_registry_operator",
"tk_438": "seller_registry_eecs_reg_db",
"tk_439": "seller_registry_account",
"tk_440": "seller_bank_vat",
"tk_441": "seller_bank_iban",
"tk_442": "seller_bank_bic_swift_code",
"tk_443": "seller_bank_account",
"tk_444": "seller_bank_name",
"tk_445": "seller_contact_email",
"tk_446": "seller_contact_fax",
"tk_447": "seller_contact_phone",
"tk_448": "seller_contact_name",
"tk_449": "seller_address_country",
"tk_450": "seller_address_town",
"tk_451": "seller_address_postalcode",
"tk_452": "seller_address_street",
"tk_453": "seller_registration_nr",
"tk_454": "seller_company",
"tk_455": "trade_identifier",
"tk_475": "earmark",
"tk_476": "minimum_validity_certif",
"tk_52": "agreement_effective_date",
"tk_720": "independent_criteria_scheme",
"tk_723": "governing_dispute_rules_of",
"tk_724": "governing_dispute_seat_arbitrator",
"tk_8010": "buyer_2_date",
"tk_8011": "buyer_2_title",
"tk_8012": "seller_2_title",
"tk_8013": "buyer_1_date",
"tk_8014": "buyer_1_title",
"tk_8015": "seller_1_title",
"tk_811": "seller_2_date",
"tk_812": "buyer_2_name",
"tk_813": "seller_2_name",
"tk_814": "seller_1_date",
"tk_815": "buyer_1_name",
"tk_816": "seller_1_name",
"tk_817": "table_04F",
"tk_818": "table_04E",
"tk_819": "table_04D",
"tk_820": "table_04C",
"tk_821": "table_04B",
"tk_822": "table_04A",
"tk_823": "table_03F",
"tk_824": "table_03E",
"tk_825": "table_03D",
"tk_826": "table_03C",
"tk_827": "table_03B",
"tk_828": "table_03A",
"tk_829": "table_06F",
"tk_830": "table_06E",
"tk_831": "table_06D",
"tk_832": "table_06C",
"tk_833": "table_06B",
"tk_834": "table_06A",
"tk_835": "table_05F",
"tk_836": "table_05E",
"tk_837": "table_05D",
"tk_838": "table_05C",
"tk_839": "table_05B",
"tk_840": "table_05A",
"tk_841": "table_08F",
"tk_842": "table_08E",
"tk_843": "table_08D",
"tk_844": "table_08C",
"tk_845": "table_08B",
"tk_846": "table_08A",
"tk_847": "table_07F",
"tk_848": "table_07E",
"tk_849": "table_07D",
"tk_850": "table_07C",
"tk_851": "table_07B",
"tk_852": "table_07A",
"tk_853": "table_14F",
"tk_854": "table_14E",
"tk_855": "table_14D",
"tk_856": "table_14C",
"tk_857": "table_14B",
"tk_858": "table_14A",
"tk_859": "table_13F",
"tk_860": "table_13E",
"tk_861": "table_13D",
"tk_862": "table_13C",
"tk_863": "table_13B",
"tk_864": "table_13A",
"tk_865": "table_12F",
"tk_866": "table_12E",
"tk_867": "table_12D",
"tk_868": "table_12C",
"tk_869": "table_12B",
"tk_870": "table_12A",
"tk_871": "table_11F",
"tk_872": "table_11E",
"tk_873": "table_11D",
"tk_874": "table_11C",
"tk_875": "table_11B",
"tk_876": "table_11A",
"tk_877": "table_10F",
"tk_878": "table_10E",
"tk_879": "table_10D",
"tk_880": "table_10C",
"tk_881": "table_10B",
"tk_882": "table_10A",
"tk_883": "table_09F",
"tk_884": "table_09E",
"tk_885": "table_09D",
"tk_886": "table_09C",
"tk_887": "table_09B",
"tk_888": "table_09A",
"tk_889": "buyer_registry_operator",
"tk_890": "buyer_registry_eecs_reg_db",
"tk_891": "buyer_registry_account",
"tk_892": "buyer_bank_vat",
"tk_893": "buyer_bank_iban",
"tk_894": "buyer_bank_bic_swift_code",
"tk_895": "buyer_bank_account",
"tk_896": "buyer_bank_name",
"tk_897": "buyer_contact_email",
"tk_898": "buyer_contact_fax",
"tk_899": "buyer_contact_phone",
"tk_900": "buyer_contact_name",
"tk_901": "buyer_address_country",
"tk_9010": "transaction_qualities_type_of_support",
"tk_9011": "transaction_qualities_commisioning_date",
"tk_902": "buyer_address_town",
"tk_903": "buyer_address_postalcode",
"tk_904": "buyer_address_street",
"tk_905": "buyer_registration_nr",
"tk_906": "buyer_company",
"tk_908": "transaction_qualities_max_greenhouse_emissions",
"tk_909": "transaction_special_conditions",
"tk_910": "domain_country_of_prod",
"tk_911": "domain_issuing_body_prod",
"tk_912": "domain_country_of_deliv",
"tk_913": "domain_issuing_body_deliv",
"tk_914": "production_device_name",
"tk_915": "production_device_number",
"tk_916": "production_device_adicional_info"

}
```
#### 3.2.2 Server
> INFO   127.0.0.1:54613 - "PUT /rec_complete HTTP/1.1" 200
#### 3.2.3 Client
> data:application/pdf;base64,JVBERi0xLjcKJeLjz9MKMSAwIG9iago8PAovUHJvZHVjZXIgKHB5cGRmKQo+ (...)

### 3.3 dotnet Client 
#### 3.3.1 server
`INFO   127.0.0.1:54715 - "GET / HTTP/1.1" 200
 INFO   127.0.0.1:54715 - "PUT /rec_complete/ HTTP/1.1" 307
 INFO   127.0.0.1:54715 - "PUT /rec_complete HTTP/1.1" 200`
#### 3.3.2
`response_GET (root): 200 {"root":"Hello World"}
 response_PUT (rec_complete/): 200`
`response_PUT_Body.pdf` as requested

## 3.b Running Similar to IIS
`uvicorn main:app --reload`
```
INFO:     127.0.0.1:56944 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:56944 - "PUT /rec_complete/ HTTP/1.1" 307 Temporary Redirect
INFO:     127.0.0.1:56944 - "PUT /rec_complete HTTP/1.1" 200 OK
```

## 4. IIS
#### 4.0.1 httpPlatformHandler v1.2 Install
https://www.iis.net/downloads/microsoft/httpplatformhandler
#### 4.0.2 Windows Features
https://stackoverflow.com/questions/9794985/config-error-this-configuration-section-cannot-be-used-at-this-path


## a-3. recover/reinstall (possible problems with python/single python installation)
1. make sure `requirements.txt` exists with the required functions
``` text
fastapi==0.115.12
uvicorn==0.34.2
PyPDFForm==2.5.0
```
2. `rm -rf venv` (Linux); `rm venv` (Powershell)
3. reinstall
```shell
mkdir venv
python -m venv .\venv\
##
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```


