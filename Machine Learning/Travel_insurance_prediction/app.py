{
 "cells": [
  {
   "cell_type": "code",
   "id": "initial_id",
   "metadata": {
    "collapsed": True,
    "ExecuteTime": {
     "end_time": "2025-05-20T19:00:55.642148Z",
     "start_time": "2025-05-20T19:00:55.341414Z"
    }
   },
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ],
   "outputs": [],
   "execution_count": 1
  },
  {
   "cell_type": "markdown",
   "id": "c6b3643e9bad33cf",
   "metadata": {},
   "source": [
    "### EDA\n",
    "Going to display basic info then check for missing values. I also will look at the summary statistics and search for unique values."
   ]
  },
  {
   "cell_type": "code",
   "id": "c89b25fc1056cd90",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-05-20T19:00:55.948483Z",
     "start_time": "2025-05-20T19:00:55.645741Z"
    }
   },
   "source": [
    "data = pd.read_csv('travel_insurance.csv')"
   ],
   "outputs": [],
   "execution_count": 2
  },
  {
   "cell_type": "code",
   "id": "6c3fa5c952842fec",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-05-20T19:00:56.111257Z",
     "start_time": "2025-05-20T19:00:56.043724Z"
    }
   },
   "source": [
    "data_info = data.info\n",
    "missing_values = data.isnull().sum()\n",
    "summary_stats = data.describe()\n",
    "unique_values = {col:data[col].unique() for col in data.columns}\n",
    "\n",
    "print(\"Data info:\\n\", data_info)\n",
    "print(\"Missing Values:\\n\", missing_values)\n",
    "print(\"summary of Statistics:\\n\", summary_stats)\n",
    "print(\"Unique values in each column:\\n\", unique_values)"
   ],
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data info:\n",
      " <bound method DataFrame.info of       Agency    Agency Type Distribution Channel  \\\n",
      "0        CBH  Travel Agency              Offline   \n",
      "1        CBH  Travel Agency              Offline   \n",
      "2        CWT  Travel Agency               Online   \n",
      "3        CWT  Travel Agency               Online   \n",
      "4        CWT  Travel Agency               Online   \n",
      "...      ...            ...                  ...   \n",
      "63321    JZI       Airlines               Online   \n",
      "63322    JZI       Airlines               Online   \n",
      "63323    JZI       Airlines               Online   \n",
      "63324    JZI       Airlines               Online   \n",
      "63325    JZI       Airlines               Online   \n",
      "\n",
      "                          Product Name Claim  Duration Destination  Net Sales  \\\n",
      "0                   Comprehensive Plan    No       186    MALAYSIA      -29.0   \n",
      "1                   Comprehensive Plan    No       186    MALAYSIA      -29.0   \n",
      "2      Rental Vehicle Excess Insurance    No        65   AUSTRALIA      -49.5   \n",
      "3      Rental Vehicle Excess Insurance    No        60   AUSTRALIA      -39.6   \n",
      "4      Rental Vehicle Excess Insurance    No        79       ITALY      -19.8   \n",
      "...                                ...   ...       ...         ...        ...   \n",
      "63321                       Basic Plan    No       111       JAPAN       35.0   \n",
      "63322                       Basic Plan    No        58       CHINA       40.0   \n",
      "63323                       Basic Plan    No         2    MALAYSIA       18.0   \n",
      "63324                       Basic Plan    No         3    VIET NAM       18.0   \n",
      "63325                       Basic Plan    No        22   HONG KONG       26.0   \n",
      "\n",
      "       Commision (in value) Gender  Age  \n",
      "0                      9.57      F   81  \n",
      "1                      9.57      F   71  \n",
      "2                     29.70    NaN   32  \n",
      "3                     23.76    NaN   32  \n",
      "4                     11.88    NaN   41  \n",
      "...                     ...    ...  ...  \n",
      "63321                 12.25      M   31  \n",
      "63322                 14.00      F   40  \n",
      "63323                  6.30      M   57  \n",
      "63324                  6.30      M   63  \n",
      "63325                  9.10      F   35  \n",
      "\n",
      "[63326 rows x 11 columns]>\n",
      "Missing Values:\n",
      " Agency                      0\n",
      "Agency Type                 0\n",
      "Distribution Channel        0\n",
      "Product Name                0\n",
      "Claim                       0\n",
      "Duration                    0\n",
      "Destination                 0\n",
      "Net Sales                   0\n",
      "Commision (in value)        0\n",
      "Gender                  45107\n",
      "Age                         0\n",
      "dtype: int64\n",
      "summary of Statistics:\n",
      "            Duration     Net Sales  Commision (in value)           Age\n",
      "count  63326.000000  63326.000000          63326.000000  63326.000000\n",
      "mean      49.317074     40.702018              9.809992     39.969981\n",
      "std      101.791566     48.845637             19.804388     14.017010\n",
      "min       -2.000000   -389.000000              0.000000      0.000000\n",
      "25%        9.000000     18.000000              0.000000     35.000000\n",
      "50%       22.000000     26.530000              0.000000     36.000000\n",
      "75%       53.000000     48.000000             11.550000     43.000000\n",
      "max     4881.000000    810.000000            283.500000    118.000000\n",
      "Unique values in each column:\n",
      " {'Agency': array(['CBH', 'CWT', 'JZI', 'KML', 'EPX', 'C2B', 'JWT', 'RAB', 'SSI',\n",
      "       'ART', 'CSR', 'CCR', 'ADM', 'LWC', 'TTW', 'TST'], dtype=object), 'Agency Type': array(['Travel Agency', 'Airlines'], dtype=object), 'Distribution Channel': array(['Offline', 'Online'], dtype=object), 'Product Name': array(['Comprehensive Plan', 'Rental Vehicle Excess Insurance',\n",
      "       'Value Plan', 'Basic Plan', 'Premier Plan',\n",
      "       '2 way Comprehensive Plan', 'Bronze Plan', 'Silver Plan',\n",
      "       'Annual Silver Plan', 'Cancellation Plan',\n",
      "       '1 way Comprehensive Plan', 'Ticket Protector', '24 Protect',\n",
      "       'Gold Plan', 'Annual Gold Plan',\n",
      "       'Single Trip Travel Protect Silver',\n",
      "       'Individual Comprehensive Plan',\n",
      "       'Spouse or Parents Comprehensive Plan',\n",
      "       'Annual Travel Protect Silver',\n",
      "       'Single Trip Travel Protect Platinum',\n",
      "       'Annual Travel Protect Gold', 'Single Trip Travel Protect Gold',\n",
      "       'Annual Travel Protect Platinum', 'Child Comprehensive Plan',\n",
      "       'Travel Cruise Protect', 'Travel Cruise Protect Family'],\n",
      "      dtype=object), 'Claim': array(['No', 'Yes'], dtype=object), 'Duration': array([ 186,   65,   60,   79,   66,   47,   63,   57,   33,    1,   53,\n",
      "          5,   39,    6,   48,   11,    3,   14,  136,   12,    7,  190,\n",
      "        364,   29,   28,  153,    4,   54,   24,    9,   45,   35,    8,\n",
      "        183,   36,   38,   13,   27,   16,   19,   18,  189,  105,   23,\n",
      "         15,  180,   90,   91,    2,   17,   10,  279,   92,   22,   64,\n",
      "         37,   31,   41,  126,   50,   55,  181,   76,   43,   56,   20,\n",
      "        164,   26,  152,   30,   32,  111,   34,  201,   62,   81,   42,\n",
      "         49,  124,  118,   52,   59,   73,   21,   25,   94,   46,   82,\n",
      "         40,  130,  388,  369,  368,  114,   85,  133,  103,  110,  147,\n",
      "        306,   75,   83,   70,  104,  131,  202,  179,   61,  365,  374,\n",
      "        386,   86,  100,  244,   99,  108,  277,  107,   87,  276,  123,\n",
      "        122,  148,  278,  204,  112,   78,   97,  142,  351,   68,  163,\n",
      "        197,   95,  125,   51,   69,   44,   71,   72,  178,   80,  150,\n",
      "         74,  171,  127,  160,  168,  158,  325,  116,  215,  149,  212,\n",
      "        282,  174,    0,  155,   67,  101,  135,   93,  328,  106,   77,\n",
      "        151,  198,  146,  266,  102,  273,  144,  175,  274,  275,   58,\n",
      "        113,  154,  117,  140,   84,  327,  115,  165,  143,  367,  159,\n",
      "         96,   98,   89,  173,  230,  269,  132,  366,  109,  192,  169,\n",
      "        268,  271,  270,  166,  431,  129,   88,  263,  185,  242,  128,\n",
      "        233,  203,  145,  170,  239,  191,  156,  182,  283,  281,  267,\n",
      "        121,  326,  370,  321,  120,  255,  403,  392,  161,  167,  288,\n",
      "        141,  223,  240,  265,  187,  397,  378,  139,  172,  229,  119,\n",
      "        134,  235, 4881,  206,  262,  261,  237,  309,  391,  137,  259,\n",
      "        243,  342,  390,  389,  157,  375,  210,  264,  200,  254,  221,\n",
      "        199,  193,  214,  218,  304,  194,  162,  250,  249,  227,  226,\n",
      "        228,  385,  246,  211,  248,  371,  387,  376,  138,  245,  377,\n",
      "        213,  417,  331,  177,  406,  207,  241,  295,  319, 4857,  373,\n",
      "        432,  208,  236,  419,  400,  196,  381,  232,  300,  314,  290,\n",
      "        176, 4847,  311,  225,  318, 4844,  184,  287,  222,  238,  310,\n",
      "        285,  216,  380,  289,  305,  384,  220,  296,  224,  209,  219,\n",
      "        382,  317,  286,  217,  407,  302,  291,  297,  260, 4831,  234,\n",
      "        205, 4829,  294,  299,  383,  324,  257,  427,  293,  284,  740,\n",
      "        334,  312,  292,  247,   -2,  303,  280, 4815,  395,  252,  253,\n",
      "        256,  195,  330,  316,  307,  323,  322,  188,  231,  372,  399,\n",
      "        315,  329,  272,  379,  411,  251,  258, 4784,  402,  436,  409,\n",
      "        547,  396,  457,  393,  394,  401,  426,  487,  408,  361,  398,\n",
      "       4738, 4736,  421,  313,  298,  456,  416,  440,  529,  461,  418,\n",
      "        420,  404,  428,  413, 4685,  430, 4652,  448,  465,  301,  478,\n",
      "        497,  405,  422,  352,  350,  545,  508,  412,  415,  437,  474,\n",
      "        441,  332, 4609,  459,   -1,  435,  472,  410,  424,  531,  434,\n",
      "       4580,  490,  494,  466,  512,  519,  444,  423,  425,  445,  414,\n",
      "        463,  433,  450,  488], dtype=int64), 'Destination': array(['MALAYSIA', 'AUSTRALIA', 'ITALY', 'UNITED STATES', 'THAILAND',\n",
      "       \"KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF\", 'NORWAY', 'VIET NAM',\n",
      "       'DENMARK', 'SINGAPORE', 'JAPAN', 'UNITED KINGDOM', 'INDONESIA',\n",
      "       'INDIA', 'CHINA', 'FRANCE', 'TAIWAN, PROVINCE OF CHINA',\n",
      "       'PHILIPPINES', 'MYANMAR', 'HONG KONG', 'KOREA, REPUBLIC OF',\n",
      "       'UNITED ARAB EMIRATES', 'NAMIBIA', 'NEW ZEALAND', 'COSTA RICA',\n",
      "       'BRUNEI DARUSSALAM', 'POLAND', 'SPAIN', 'CZECH REPUBLIC',\n",
      "       'GERMANY', 'SRI LANKA', 'CAMBODIA', 'AUSTRIA', 'SOUTH AFRICA',\n",
      "       'TANZANIA, UNITED REPUBLIC OF', \"LAO PEOPLE'S DEMOCRATIC REPUBLIC\",\n",
      "       'NEPAL', 'NETHERLANDS', 'MACAO', 'CROATIA', 'FINLAND', 'CANADA',\n",
      "       'TUNISIA', 'RUSSIAN FEDERATION', 'GREECE', 'BELGIUM', 'IRELAND',\n",
      "       'SWITZERLAND', 'CHILE', 'ISRAEL', 'BANGLADESH', 'ICELAND',\n",
      "       'PORTUGAL', 'ROMANIA', 'KENYA', 'GEORGIA', 'TURKEY', 'SWEDEN',\n",
      "       'MALDIVES', 'ESTONIA', 'SAUDI ARABIA', 'PAKISTAN', 'QATAR', 'PERU',\n",
      "       'LUXEMBOURG', 'MONGOLIA', 'ARGENTINA', 'CYPRUS', 'FIJI',\n",
      "       'BARBADOS', 'TRINIDAD AND TOBAGO', 'ETHIOPIA', 'PAPUA NEW GUINEA',\n",
      "       'SERBIA', 'JORDAN', 'ECUADOR', 'BENIN', 'OMAN', 'BAHRAIN',\n",
      "       'UGANDA', 'BRAZIL', 'MEXICO', 'HUNGARY', 'AZERBAIJAN', 'MOROCCO',\n",
      "       'URUGUAY', 'MAURITIUS', 'JAMAICA', 'KAZAKHSTAN', 'GHANA',\n",
      "       'UZBEKISTAN', 'SLOVENIA', 'KUWAIT', 'GUAM', 'BULGARIA',\n",
      "       'LITHUANIA', 'NEW CALEDONIA', 'EGYPT', 'ARMENIA', 'BOLIVIA',\n",
      "       'VIRGIN ISLANDS, U.S.', 'PANAMA', 'SIERRA LEONE', 'COLOMBIA',\n",
      "       'PUERTO RICO', 'UKRAINE', 'GUINEA', 'GUADELOUPE',\n",
      "       'MOLDOVA, REPUBLIC OF', 'GUYANA', 'LATVIA', 'ZIMBABWE', 'VANUATU',\n",
      "       'VENEZUELA', 'BOTSWANA', 'BERMUDA', 'MALI', 'KYRGYZSTAN',\n",
      "       'CAYMAN ISLANDS', 'MALTA', 'LEBANON', 'REUNION', 'SEYCHELLES',\n",
      "       'ZAMBIA', 'SAMOA', 'NORTHERN MARIANA ISLANDS', 'NIGERIA',\n",
      "       'DOMINICAN REPUBLIC', 'TAJIKISTAN', 'ALBANIA',\n",
      "       'MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF',\n",
      "       'LIBYAN ARAB JAMAHIRIYA', 'ANGOLA', 'BELARUS',\n",
      "       'TURKS AND CAICOS ISLANDS', 'FAROE ISLANDS', 'TURKMENISTAN',\n",
      "       'GUINEA-BISSAU', 'CAMEROON', 'BHUTAN', 'RWANDA', 'SOLOMON ISLANDS',\n",
      "       'IRAN, ISLAMIC REPUBLIC OF', 'GUATEMALA', 'FRENCH POLYNESIA',\n",
      "       'TIBET', 'SENEGAL', 'REPUBLIC OF MONTENEGRO',\n",
      "       'BOSNIA AND HERZEGOVINA'], dtype=object), 'Net Sales': array([-29.  , -49.5 , -39.6 , ...,   1.74, 388.8 ,  11.58]), 'Commision (in value)': array([ 9.57, 29.7 , 23.76, ..., 21.63, 97.2 ,  3.25]), 'Gender': array(['F', nan, 'M'], dtype=object), 'Age': array([ 81,  71,  32,  41,  44,  29,  37, 118,  47,  48,  64,  36,  53,\n",
      "        43,  58,  25,  34,  26,  30,  33,  35,  31,  61,  20,  46,  49,\n",
      "        50,  62,  65,  24,  40,  21,  66,  57,  45,  52,  60,  27,  23,\n",
      "        39,  59,  28,  67,  38,  72,  51,  55,  54,  69,  22,  78,  42,\n",
      "        70,  68,  77,  63,  56,  79,  76,  16,  14,  73,  18,  19,  74,\n",
      "        85,  84,  13,  75,  87,  80,  83,  12,  10,   8,  17,  15,   9,\n",
      "        11,  86,   3,  82,   1,   5,  88,   2,   4,   0,   7], dtype=int64)}\n"
     ]
    }
   ],
   "execution_count": 3
  },
  {
   "cell_type": "markdown",
   "id": "c5c3702f72a79fd7",
   "metadata": {},
   "source": [
    "Needed to check if there are any whitespaces within the column titles. Also moving forward, I will not use print function(), that was a lot of unnecessary typing. Idk what I was thinking really when it is easier to output the results using callback."
   ]
  },
  {
   "cell_type": "code",
   "id": "f0fb70ffd6c9a165",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-05-20T19:00:56.175642Z",
     "start_time": "2025-05-20T19:00:56.157836Z"
    }
   },
   "source": [
    "data.columns.str.isspace()"
   ],
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([False, False, False, False, False, False, False, False, False,\n",
       "       False, False])"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "execution_count": 4
  },
  {
   "cell_type": "markdown",
   "id": "809c539000c7c4a4",
   "metadata": {},
   "source": [
    "### Data Cleaning and feature Engineering\n",
    "Address the null values in gender \\\n",
    "Encode target variable as binary \\\n",
    "create a new net sales revenue feature because net sales - commission equals total profit after commission\\\n",
    "Hot encode categorical features\\\n",
    "Check results"
   ]
  },
  {
   "cell_type": "code",
   "id": "fdfb84f34538571f",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-05-20T19:00:56.343870Z",
     "start_time": "2025-05-20T19:00:56.239323Z"
    }
   },
   "source": [
    "data['Gender'] = data['Gender'].fillna('Unknown')\n",
    "data['Claim'] = data['Claim'].map({'Yes':1, 'No':0})\n",
    "\n",
    "\n",
    "data.rename(columns={'Commision (in value)': 'Commission'}, inplace=True)\n",
    "data[\"profit\"] = data['Net Sales'] - data['Commission']\n",
    "\n",
    "categorical_features = ['Agency', 'Agency Type', 'Distribution Channel', 'Product Name', 'Destination', 'Gender']\n",
    "data_encoded = pd.get_dummies(data, columns=categorical_features, drop_first=True)\n",
    "\n",
    "data_encoded.info()\n",
    "data_encoded.head()"
   ],
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 63326 entries, 0 to 63325\n",
      "Columns: 198 entries, Claim to Gender_Unknown\n",
      "dtypes: bool(192), float64(3), int64(3)\n",
      "memory usage: 14.5 MB\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "   Claim  Duration  Net Sales  Commission  Age  profit  Agency_ART  \\\n",
       "0      0       186      -29.0        9.57   81  -38.57       False   \n",
       "1      0       186      -29.0        9.57   71  -38.57       False   \n",
       "2      0        65      -49.5       29.70   32  -79.20       False   \n",
       "3      0        60      -39.6       23.76   32  -63.36       False   \n",
       "4      0        79      -19.8       11.88   41  -31.68       False   \n",
       "\n",
       "   Agency_C2B  Agency_CBH  Agency_CCR  ...  Destination_URUGUAY  \\\n",
       "0       False        True       False  ...                False   \n",
       "1       False        True       False  ...                False   \n",
       "2       False       False       False  ...                False   \n",
       "3       False       False       False  ...                False   \n",
       "4       False       False       False  ...                False   \n",
       "\n",
       "   Destination_UZBEKISTAN  Destination_VANUATU  Destination_VENEZUELA  \\\n",
       "0                   False                False                  False   \n",
       "1                   False                False                  False   \n",
       "2                   False                False                  False   \n",
       "3                   False                False                  False   \n",
       "4                   False                False                  False   \n",
       "\n",
       "   Destination_VIET NAM  Destination_VIRGIN ISLANDS, U.S.  Destination_ZAMBIA  \\\n",
       "0                 False                             False               False   \n",
       "1                 False                             False               False   \n",
       "2                 False                             False               False   \n",
       "3                 False                             False               False   \n",
       "4                 False                             False               False   \n",
       "\n",
       "   Destination_ZIMBABWE  Gender_M  Gender_Unknown  \n",
       "0                 False     False           False  \n",
       "1                 False     False           False  \n",
       "2                 False     False            True  \n",
       "3                 False     False            True  \n",
       "4                 False     False            True  \n",
       "\n",
       "[5 rows x 198 columns]"
      ],
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Claim</th>\n",
       "      <th>Duration</th>\n",
       "      <th>Net Sales</th>\n",
       "      <th>Commission</th>\n",
       "      <th>Age</th>\n",
       "      <th>profit</th>\n",
       "      <th>Agency_ART</th>\n",
       "      <th>Agency_C2B</th>\n",
       "      <th>Agency_CBH</th>\n",
       "      <th>Agency_CCR</th>\n",
       "      <th>...</th>\n",
       "      <th>Destination_URUGUAY</th>\n",
       "      <th>Destination_UZBEKISTAN</th>\n",
       "      <th>Destination_VANUATU</th>\n",
       "      <th>Destination_VENEZUELA</th>\n",
       "      <th>Destination_VIET NAM</th>\n",
       "      <th>Destination_VIRGIN ISLANDS, U.S.</th>\n",
       "      <th>Destination_ZAMBIA</th>\n",
       "      <th>Destination_ZIMBABWE</th>\n",
       "      <th>Gender_M</th>\n",
       "      <th>Gender_Unknown</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>186</td>\n",
       "      <td>-29.0</td>\n",
       "      <td>9.57</td>\n",
       "      <td>81</td>\n",
       "      <td>-38.57</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>...</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>186</td>\n",
       "      <td>-29.0</td>\n",
       "      <td>9.57</td>\n",
       "      <td>71</td>\n",
       "      <td>-38.57</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>...</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "      <td>65</td>\n",
       "      <td>-49.5</td>\n",
       "      <td>29.70</td>\n",
       "      <td>32</td>\n",
       "      <td>-79.20</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>...</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>60</td>\n",
       "      <td>-39.6</td>\n",
       "      <td>23.76</td>\n",
       "      <td>32</td>\n",
       "      <td>-63.36</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>...</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>79</td>\n",
       "      <td>-19.8</td>\n",
       "      <td>11.88</td>\n",
       "      <td>41</td>\n",
       "      <td>-31.68</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>...</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 198 columns</p>\n",
       "</div>"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "execution_count": 5
  },
  {
   "cell_type": "markdown",
   "id": "1b9173e3956dc455",
   "metadata": {},
   "source": [
    "### Classifying the model\n",
    "split into features first, train test split the data, using random forest to train the classifier, make predictions, and then evaluate"
   ]
  },
  {
   "cell_type": "code",
   "id": "92f0f0fbc1451281",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-05-20T19:01:17.193834Z",
     "start_time": "2025-05-20T19:00:59.141603Z"
    }
   },
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.metrics import classification_report, confusion_matrix\n",
    "\n",
    "X = data_encoded.drop('Claim', axis=1)\n",
    "y = data_encoded['Claim']\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "clf = RandomForestClassifier(random_state=42)\n",
    "clf.fit(X_train, y_train)\n",
    "\n",
    "y_pred = clf.predict(X_test)\n",
    "\n",
    "conf_matrix = confusion_matrix(y_test, y_pred)\n",
    "class_report = classification_report(y_test, y_pred)\n",
    "\n",
    "(conf_matrix, class_report)"
   ],
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([[12443,    43],\n",
       "        [  177,     3]], dtype=int64),\n",
       " '              precision    recall  f1-score   support\\n\\n           0       0.99      1.00      0.99     12486\\n           1       0.07      0.02      0.03       180\\n\\n    accuracy                           0.98     12666\\n   macro avg       0.53      0.51      0.51     12666\\nweighted avg       0.97      0.98      0.98     12666\\n')"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "execution_count": 6
  },
  {
   "cell_type": "markdown",
   "id": "9187b2d98aa81fe3",
   "metadata": {},
   "source": [
    "I rescind my previous statement. Above results are looking quite sloppy."
   ]
  },
  {
   "cell_type": "code",
   "id": "d3aaf7e69e0f3b9",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-05-20T19:01:17.246653Z",
     "start_time": "2025-05-20T19:01:17.226134Z"
    }
   },
   "source": [
    "print(class_report)\n",
    "print(conf_matrix)"
   ],
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.99      1.00      0.99     12486\n",
      "           1       0.07      0.02      0.03       180\n",
      "\n",
      "    accuracy                           0.98     12666\n",
      "   macro avg       0.53      0.51      0.51     12666\n",
      "weighted avg       0.97      0.98      0.98     12666\n",
      "\n",
      "[[12443    43]\n",
      " [  177     3]]\n"
     ]
    }
   ],
   "execution_count": 7
  },
  {
   "cell_type": "markdown",
   "id": "5878495f757ce946",
   "metadata": {},
   "source": [
    "Evaluation: the model shows high accuracy, precision, and recall for claims 0 but performs poorly on accuracy, recall, and precision for claims 1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "265f38910c2c0dbf",
   "metadata": {},
   "source": [
    "### Model Tuning\n",
    "I am choosing to use Random search for efficiency, performance, and scalability. I also decided to Subsample the dataset to 10% of its original size to reduce execution time. There is a substantial amount of records with multiple features to process, and I am just a student with a not so high performing laptop. Lastly, I am starting over from scratch because my vertigo is not okay with the constant scrolling right now."
   ]
  },
  {
   "cell_type": "code",
   "id": "969af1ac43624088",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-05-20T19:01:22.100132Z",
     "start_time": "2025-05-20T19:01:17.538521Z"
    }
   },
   "source": [
    "from sklearn.model_selection import RandomizedSearchCV, train_test_split\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.preprocessing import OneHotEncoder\n",
    "from sklearn.compose import ColumnTransformer\n",
    "\n",
    "df = pd.read_csv('travel_insurance.csv')\n",
    "df['Gender'] = df['Gender'].fillna('Unknown')\n",
    "df['Claim'] = df['Claim'].apply(lambda x: 1 if x == 'Yes' else 0)\n",
    "\n",
    "\n",
    "categorical_columns = ['Agency', 'Agency Type', 'Distribution Channel', 'Product Name', 'Gender', 'Destination']\n",
    "preprocessor = ColumnTransformer(transformers=[('onehot', OneHotEncoder(sparse=False, handle_unknown='ignore'), categorical_columns)],remainder='passthrough')\n",
    "\n",
    "subsampled_data = df.sample(frac=0.1, random_state=42)\n",
    "\n",
    "X = subsampled_data.drop('Claim', axis=1)\n",
    "y = subsampled_data['Claim']\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "X_train_encoded = preprocessor.fit_transform(X_train)\n",
    "\n",
    "param_dist = {\n",
    "    'n_estimators': [50, 100, 150],\n",
    "    'max_depth': [5, 10, None],\n",
    "    'min_samples_split': [2, 5],\n",
    "    'min_samples_leaf': [1, 2],\n",
    "    'bootstrap': [True, False]\n",
    "}\n",
    "\n",
    "rf = RandomForestClassifier(random_state=42)\n",
    "\n",
    "random_search = RandomizedSearchCV(\n",
    "    estimator=rf,\n",
    "    param_distributions=param_dist,\n",
    "    n_iter=5,\n",
    "    cv=3,\n",
    "    verbose=2,\n",
    "    random_state=42,\n",
    "    n_jobs=-1\n",
    ")\n",
    "\n",
    "random_search.fit(X_train_encoded, y_train)\n",
    "\n",
    "print(f\"Best parameters: {random_search.best_params_}\")\n",
    "print(f\"Best cross-validation score: {random_search.best_score_:.2f}\")"
   ],
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fitting 3 folds for each of 5 candidates, totalling 15 fits\n",
      "Best parameters: {'n_estimators': 100, 'min_samples_split': 5, 'min_samples_leaf': 1, 'max_depth': 5, 'bootstrap': True}\n",
      "Best cross-validation score: 0.99\n"
     ]
    }
   ],
   "execution_count": 8
  },
  {
   "cell_type": "code",
   "id": "a4dc2de24054cc84",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-05-20T19:04:29.126080Z",
     "start_time": "2025-05-20T19:04:21.599411Z"
    }
   },
   "source": [
    "data = pd.read_csv('travel_insurance.csv')\n",
    "\n",
    "data_info = data.info\n",
    "missing_values = data.isnull().sum()\n",
    "summary_stats = data.describe()\n",
    "unique_values = {col:data[col].unique() for col in data.columns}\n",
    "\n",
    "data.columns.str.isspace()\n",
    "\n",
    "data['Gender'] = data['Gender'].fillna('Unknown')\n",
    "data['Claim'] = data['Claim'].map({'Yes':1, 'No':0})\n",
    "\n",
    "\n",
    "data.rename(columns={'Commision (in value)': 'Commission'}, inplace=True)\n",
    "data[\"profit\"] = data['Net Sales'] - data['Commission']\n",
    "\n",
    "categorical_features = ['Agency', 'Agency Type', 'Distribution Channel', 'Product Name', 'Destination', 'Gender']\n",
    "data_encoded = pd.get_dummies(data, columns=categorical_features, drop_first=True)\n",
    "\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.metrics import classification_report, confusion_matrix\n",
    "\n",
    "X = data_encoded.drop('Claim', axis=1)\n",
    "y = data_encoded['Claim']\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "clf = RandomForestClassifier(random_state=42)\n",
    "clf.fit(X_train, y_train)\n",
    "\n",
    "y_pred = clf.predict(X_test)\n",
    "\n",
    "from sklearn.model_selection import RandomizedSearchCV, train_test_split\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.preprocessing import OneHotEncoder\n",
    "from sklearn.compose import ColumnTransformer\n",
    "\n",
    "df = pd.read_csv('travel_insurance.csv')\n",
    "df['Gender'] = df['Gender'].fillna('Unknown')\n",
    "df['Claim'] = df['Claim'].apply(lambda x: 1 if x == 'Yes' else 0)\n",
    "\n",
    "\n",
    "categorical_columns = ['Agency', 'Agency Type', 'Distribution Channel', 'Product Name', 'Gender', 'Destination']\n",
    "preprocessor = ColumnTransformer(transformers=[('onehot', OneHotEncoder(sparse=False, handle_unknown='ignore'), categorical_columns)],remainder='passthrough')\n",
    "\n",
    "subsampled_data = df.sample(frac=0.1, random_state=42)\n",
    "\n",
    "X = subsampled_data.drop('Claim', axis=1)\n",
    "y = subsampled_data['Claim']\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "X_train_encoded = preprocessor.fit_transform(X_train)\n",
    "\n",
    "param_dist = {\n",
    "    'n_estimators': [50, 100, 150],\n",
    "    'max_depth': [5, 10, None],\n",
    "    'min_samples_split': [2, 5],\n",
    "    'min_samples_leaf': [1, 2],\n",
    "    'bootstrap': [True, False]\n",
    "}\n",
    "\n",
    "rf = RandomForestClassifier(random_state=42)\n",
    "\n",
    "random_search = RandomizedSearchCV(\n",
    "    estimator=rf,\n",
    "    param_distributions=param_dist,\n",
    "    n_iter=5,\n",
    "    cv=3,\n",
    "    verbose=2,\n",
    "    random_state=42,\n",
    "    n_jobs=-1\n",
    ")\n",
    "\n",
    "random_search.fit(X_train_encoded, y_train)"
   ],
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fitting 3 folds for each of 5 candidates, totalling 15 fits\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "RandomizedSearchCV(cv=3, estimator=RandomForestClassifier(random_state=42),\n",
       "                   n_iter=5, n_jobs=-1,\n",
       "                   param_distributions={'bootstrap': [True, False],\n",
       "                                        'max_depth': [5, 10, None],\n",
       "                                        'min_samples_leaf': [1, 2],\n",
       "                                        'min_samples_split': [2, 5],\n",
       "                                        'n_estimators': [50, 100, 150]},\n",
       "                   random_state=42, verbose=2)"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "execution_count": 10
  },
  {
   "metadata": {},
   "cell_type": "markdown",
   "source": "#### Streamlit App",
   "id": "410314963f151015"
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-05-20T19:04:52.851838Z",
     "start_time": "2025-05-20T19:04:48.822572Z"
    }
   },
   "cell_type": "code",
   "source": "pip install streamlit pandas numpy scikit-learn",
   "id": "d999415caa5f3e65",
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in c:\\users\\isisv\\anaconda3\\lib\\site-packages (1.42.2)\n",
      "Requirement already satisfied: pandas in c:\\users\\isisv\\anaconda3\\lib\\site-packages (2.2.3)\n",
      "Requirement already satisfied: numpy in c:\\users\\isisv\\anaconda3\\lib\\site-packages (1.23.5)\n",
      "Requirement already satisfied: scikit-learn in c:\\users\\isisv\\anaconda3\\lib\\site-packages (1.0.2)\n",
      "Requirement already satisfied: altair<6,>=4.0 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from streamlit) (5.5.0)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from streamlit) (1.9.0)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from streamlit) (5.5.2)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from streamlit) (8.0.4)\n",
      "Requirement already satisfied: packaging<25,>=20 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from streamlit) (21.3)\n",
      "Requirement already satisfied: pillow<12,>=7.1.0 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from streamlit) (9.2.0)\n",
      "Requirement already satisfied: protobuf<6,>=3.20 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from streamlit) (5.28.3)\n",
      "Requirement already satisfied: pyarrow>=7.0 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from streamlit) (18.1.0)\n",
      "Requirement already satisfied: requests<3,>=2.27 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from streamlit) (2.32.3)\n",
      "Requirement already satisfied: rich<14,>=10.14.0 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from streamlit) (13.8.0)\n",
      "Requirement already satisfied: tenacity<10,>=8.1.0 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from streamlit) (9.0.0)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.4.0 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from streamlit) (4.12.2)\n",
      "Requirement already satisfied: watchdog<7,>=2.1.5 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from streamlit) (2.1.6)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from streamlit) (3.1.44)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from streamlit) (0.9.1)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from streamlit) (6.1)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from pandas) (2.8.2)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from pandas) (2024.2)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from pandas) (2024.2)\n",
      "Requirement already satisfied: scipy>=1.1.0 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from scikit-learn) (1.9.1)\n",
      "Requirement already satisfied: joblib>=0.11 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from scikit-learn) (1.1.0)\n",
      "Requirement already satisfied: threadpoolctl>=2.0.0 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from scikit-learn) (2.2.0)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (2.11.3)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.16.0)\n",
      "Requirement already satisfied: narwhals>=1.14.2 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (1.28.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
      "Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from packaging<25,>=20->streamlit) (3.0.9)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.3)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (1.26.11)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2022.9.14)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (3.0.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.18.0)\n",
      "Requirement already satisfied: smmap<6,>=3.0.1 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)\n",
      "Requirement already satisfied: MarkupSafe>=0.23 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.0.1)\n",
      "Requirement already satisfied: attrs>=17.4.0 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (21.4.0)\n",
      "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.18.0)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\users\\isisv\\anaconda3\\lib\\site-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.2)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip is available: 25.0.1 -> 25.1.1\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "execution_count": 12
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-05-20T19:05:02.218644Z",
     "start_time": "2025-05-20T19:05:02.202567Z"
    }
   },
   "cell_type": "code",
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "from sklearn.model_selection import train_test_split, RandomizedSearchCV\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.metrics import classification_report, confusion_matrix\n",
    "from sklearn.preprocessing import OneHotEncoder\n",
    "from sklearn.compose import ColumnTransformer\n",
    "\n",
    "st.title(\"Travel Insurance Claim Prediction App\")\n"
   ],
   "id": "4dcea4d66783ddd6",
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-05-20 12:05:02.202 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:02.202 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "execution_count": 13
  },
  {
   "metadata": {},
   "cell_type": "markdown",
   "source": "Data upload and exploration",
   "id": "9f6d757979ce83d7"
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-05-20T19:05:11.416155Z",
     "start_time": "2025-05-20T19:05:11.400355Z"
    }
   },
   "cell_type": "code",
   "source": [
    "uploaded_file = st.file_uploader(\"Upload your travel_insurance.csv file\", type=\"csv\")\n",
    "if uploaded_file is not None:\n",
    "    data = pd.read_csv(uploaded_file)\n",
    "    st.write(\"First 5 rows of your data:\")\n",
    "    st.dataframe(data.head())\n"
   ],
   "id": "4455882b4901f035",
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-05-20 12:05:11.400 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:11.400 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:11.400 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:11.400 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:11.400 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "execution_count": 14
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-05-20T19:05:17.462739Z",
     "start_time": "2025-05-20T19:05:17.352191Z"
    }
   },
   "cell_type": "code",
   "source": [
    "    st.subheader(\"Data Information\")\n",
    "    st.write(data.info())\n",
    "    st.write(\"Missing Values:\", data.isnull().sum())\n",
    "    st.write(\"Summary Statistics:\")\n",
    "    st.write(data.describe())\n",
    "    st.write(\"Unique Values per Column:\")\n",
    "    st.write({col: data[col].unique() for col in data.columns})\n"
   ],
   "id": "b9ce297a3259051",
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-05-20 12:05:17.356 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:17.358 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:17.368 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:17.368 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:17.368 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:17.368 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:17.383 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:17.383 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:17.383 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:17.383 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:17.404 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:17.404 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:17.406 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:17.406 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:17.406 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:17.408 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:17.415 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:17.415 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:17.415 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:17.415 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:17.431 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:17.431 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:17.446 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:17.446 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 63326 entries, 0 to 63325\n",
      "Data columns (total 12 columns):\n",
      " #   Column                Non-Null Count  Dtype  \n",
      "---  ------                --------------  -----  \n",
      " 0   Agency                63326 non-null  object \n",
      " 1   Agency Type           63326 non-null  object \n",
      " 2   Distribution Channel  63326 non-null  object \n",
      " 3   Product Name          63326 non-null  object \n",
      " 4   Claim                 63326 non-null  int64  \n",
      " 5   Duration              63326 non-null  int64  \n",
      " 6   Destination           63326 non-null  object \n",
      " 7   Net Sales             63326 non-null  float64\n",
      " 8   Commission            63326 non-null  float64\n",
      " 9   Gender                63326 non-null  object \n",
      " 10  Age                   63326 non-null  int64  \n",
      " 11  profit                63326 non-null  float64\n",
      "dtypes: float64(3), int64(3), object(6)\n",
      "memory usage: 5.8+ MB\n"
     ]
    }
   ],
   "execution_count": 15
  },
  {
   "metadata": {},
   "cell_type": "markdown",
   "source": "Data Cleaning and feature engineering in streamlit to show results interactively",
   "id": "6ac8c99e6113fa05"
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-05-20T19:05:23.525090Z",
     "start_time": "2025-05-20T19:05:23.448037Z"
    }
   },
   "cell_type": "code",
   "source": [
    "    # Fill missing Gender\n",
    "    data['Gender'] = data['Gender'].fillna('Unknown')\n",
    "    # Encode Claim\n",
    "    data['Claim'] = data['Claim'].map({'Yes': 1, 'No': 0})\n",
    "    # Rename columns and compute profit\n",
    "    if 'Commision (in value)' in data.columns:\n",
    "        data.rename(columns={'Commision (in value)': 'Commission'}, inplace=True)\n",
    "    if 'Net Sales' in data.columns and 'Commission' in data.columns:\n",
    "        data['profit'] = data['Net Sales'] - data['Commission']\n",
    "    # One-hot encode categorical features\n",
    "    categorical_features = ['Agency', 'Agency Type', 'Distribution Channel', 'Product Name', 'Destination', 'Gender']\n",
    "    data_encoded = pd.get_dummies(data, columns=categorical_features, drop_first=True)\n",
    "    st.write(\"Encoded Data Preview:\")\n",
    "    st.dataframe(data_encoded.head())\n"
   ],
   "id": "f3ad36167657b478",
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-05-20 12:05:23.493 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:23.493 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:23.493 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:23.493 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:23.509 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:23.509 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "execution_count": 16
  },
  {
   "metadata": {},
   "cell_type": "markdown",
   "source": "Button for model training and evaluating",
   "id": "37974816017684d1"
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-05-20T19:05:29.974204Z",
     "start_time": "2025-05-20T19:05:29.958531Z"
    }
   },
   "cell_type": "code",
   "source": [
    "    if st.button(\"Train Random Forest Model\"):\n",
    "        X = data_encoded.drop('Claim', axis=1)\n",
    "        y = data_encoded['Claim']\n",
    "        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "        clf = RandomForestClassifier(random_state=42)\n",
    "        clf.fit(X_train, y_train)\n",
    "        y_pred = clf.predict(X_test)\n",
    "        st.write(\"Classification Report:\")\n",
    "        st.text(classification_report(y_test, y_pred))\n",
    "        st.write(\"Confusion Matrix:\")\n",
    "        st.write(confusion_matrix(y_test, y_pred))\n"
   ],
   "id": "ccbf1506a5603760",
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-05-20 12:05:29.958 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:29.958 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:29.958 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:29.958 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:29.966 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "execution_count": 17
  },
  {
   "metadata": {},
   "cell_type": "markdown",
   "source": "Allowing users to run hyperparameter tuning with randomizedsearchcv",
   "id": "97367a70636c3171"
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-05-20T19:05:34.307078Z",
     "start_time": "2025-05-20T19:05:34.291185Z"
    }
   },
   "cell_type": "code",
   "source": [
    "    if st.button(\"Tune Model (RandomizedSearchCV)\"):\n",
    "        param_dist = {\n",
    "            'n_estimators': [50, 100, 150],\n",
    "            'max_depth': [5, 10, None],\n",
    "            'min_samples_split': [2, 5],\n",
    "            'min_samples_leaf': [1, 2],\n",
    "            'bootstrap': [True, False]\n",
    "        }\n",
    "        rf = RandomForestClassifier(random_state=42)\n",
    "        random_search = RandomizedSearchCV(\n",
    "            estimator=rf,\n",
    "            param_distributions=param_dist,\n",
    "            n_iter=5,\n",
    "            cv=3,\n",
    "            verbose=2,\n",
    "            random_state=42,\n",
    "            n_jobs=-1\n",
    "        )\n",
    "        random_search.fit(X_train, y_train)\n",
    "        st.write(f\"Best parameters: {random_search.best_params_}\")\n",
    "        st.write(f\"Best cross-validation score: {random_search.best_score_:.2f}\")\n"
   ],
   "id": "4f8ff70ded6ed45",
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-05-20 12:05:34.291 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:34.291 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:34.291 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:34.291 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-20 12:05:34.291 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "execution_count": 18
  },
  {
   "metadata": {},
   "cell_type": "markdown",
   "source": "Save script as app.py and run the app in bash using the code below.",
   "id": "a727267130f2adc3"
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-05-20T19:07:36.369132Z",
     "start_time": "2025-05-20T19:07:36.360605Z"
    }
   },
   "cell_type": "code",
   "source": "# streamlit run app.py",
   "id": "98cba8263ae19845",
   "outputs": [],
   "execution_count": 21
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
