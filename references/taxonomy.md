# Taxonomy - Portfolio123 Reference

The Taxonomy category covers the ETF classification vocabularies. Each of the
eight dimensions (asset class, country, family, method, region, sector, size,
style) is exposed as a pair: a string factor that returns the ETF's code for
that dimension, and a `...Set(...)` membership function that tests the ETF's
code against a list you supply. These factors and functions apply to ETF
contexts only - they classify exchange-traded funds, not ordinary equities. For
stock industry and sector classification (RBICS) see
[industry-sector.md](industry-sector.md).

Coverage: 8 functions / 8 factors - extracted from the official Factor Reference
on 2026-06-09. The code tables below are reproduced verbatim from each factor's
detail page.

## Contents

- [ETF Asset Class](#etf-asset-class)
- [ETF Country](#etf-country)
- [ETF Family](#etf-family)
- [ETF Method](#etf-method)
- [ETF Region](#etf-region)
- [ETF Sector](#etf-sector)
- [ETF Size](#etf-size)
- [ETF Style](#etf-style)
- [Common Mistakes](#common-mistakes)
- [See Also](#see-also)

## ETF Asset Class

#### `ETFAssetClass`
Returns the ETF's assetclass code as a string. Applies to ETFs only; for ordinary stocks it returns no value.

#### `ETFAssetClassSet(x1[, x2..x30])`
Evaluates to true when the ETF's assetclass matches any of the up to 30 codes passed as arguments. Applies to ETFs only.

Valid assetclass codes (use these string values as the function arguments):

| AssetClass | Code |
|---|---|
| Alternative | ALTERN |
| Commodities | COMMOD |
| Currencies | CURR |
| Equity | EQUITY |
| Fixed Income | FIXINC |
| Mixed Assets | MIXASST |

## ETF Country

#### `ETFCountry`
Returns the ETF's country code as a string. Applies to ETFs only; for ordinary stocks it returns no value.

#### `ETFCountrySet(x1[, x2..x30])`
Evaluates to true when the ETF's country matches any of the up to 30 codes passed as arguments. Applies to ETFs only.

Valid country codes (use these string values as the function arguments):

| Country | Code |
|---|---|
| Afghanistan | AFGHAN |
| Albania | ALBANIA |
| Algeria | ALGERIA |
| American Samoa | AMSAMOA |
| Andorra | ANDORRA |
| Angola | ANGOLA |
| Anguilla | ANGUILLA |
| Antigua And Barbuda | ANTIGUA |
| Argentina | ARGENTNA |
| Armenia | ARMENIA |
| Aruba | ARUBA |
| Australia | AUSTRALIA |
| Austria | AUSTRIA |
| Azerbaijan | AZERBAJN |
| Bahamas | BAHAMAS |
| Bahrain | BAHRAIN |
| Bangladesh | BANGLAD |
| Barbados | BARBADOS |
| Belarus | BELARUS |
| Belgium | BELGIUM |
| Belize | BELIZE |
| Benin | BENIN |
| Bermuda | BERMUDA |
| Bhutan | BHUTAN |
| Bolivia | BOLIVIA |
| Bosnia And Herzegowina | BOSHERZEG |
| Botswana | BOTSWANA |
| Brazil | BRAZIL |
| Brunei Darussalam | BRUNEI |
| Bulgaria | BULGARIA |
| Burkina Faso | BURKFASO |
| Burundi | BURUNDI |
| Cambodia | CAMBODIA |
| Cameroon | CAMEROON |
| Canada | CANADA |
| Cape Verde | CAPEVERDE |
| Cayman Islands | CAYMAN |
| Central African Republic | CENAFRICA |
| Chad | CHAD |
| Chile | CHILE |
| China | CHINA |
| Christmas Island | CHRISTMAS |
| Cocos (keeling) Islands | COCOS |
| Colombia | COLOMBIA |
| Comoros | COMOROS |
| Congo | CONGO |
| Cook Islands | COOK |
| Costa Rica | COSTARICA |
| Cote D Ivoire | COTEIVOIR |
| Croatia (hrvatska) | CROATIA |
| Cuba | CUBA |
| Cyprus | CYPRUS |
| Czech Republic | CZECH |
| Denmark | DENMARK |
| Djibouti | DJIBOUTI |
| Dominica | DOMINICA |
| Dominican Republic | DOMINICAN |
| Ecuador | ECUADOR |
| Egypt | EGYPT |
| El Salvador | ELSALVADR |
| Equatorial Guinea | EQGUINEA |
| Eritrea | ERITREA |
| Estonia | ESTONIA |
| Ethiopia | ETHIOPIA |
| Falkland (malvinas) Islands | FALKLAND |
| Faroe Islands | FAROE |
| Fed. Sts Of Micronesia | MICRONES |
| Fiji | FIJI |
| Finland | FINLAND |
| France | FRANCE |
| French Guiana | FRGUIANA |
| French Polynesia | FRPOLYNES |
| Gabon | GABON |
| Gambia | GAMBIA |
| Georgia | GEORGIA |
| Germany | GERMANY |
| Ghana | GHANA |
| Gibraltar | GIBRALTAR |
| Greece | GREECE |
| Greenland | GREENLAND |
| Grenada | GRENADA |
| Guadeloupe | GUADELOUP |
| Guam | GUAM |
| Guatemala | GUATEMALA |
| Guinea-bissau | GUINEABIS |
| Guyana | GUYANA |
| Haiti | HAITI |
| Holy See (vatican City State) | HOLYSEE |
| Honduras | HONDURAS |
| Hong Kong | HONGKONG |
| Hungary | HUNGARY |
| Iceland | ICELAND |
| India | INDIA |
| Indonesia | INDONESIA |
| Iran | IRAN |
| Iraq | IRAQ |
| Ireland | IRELAND |
| Israel | ISRAEL |
| Italy | ITALY |
| Jamaica | JAMAICA |
| Japan | JAPAN |
| Jordan | JORDAN |
| Kazakhstan | KAZAKH |
| Kenya | KENYA |
| Kiribati | KIRIBATI |
| Kuwait | KUWAIT |
| Kyrgyzstan | KYRGY |
| Laos | LAOS |
| Latvia | LATVIA |
| Lebanon | LEBANON |
| Lesotho | LESOTHO |
| Liberia | LIBERIA |
| Libya | LIBYA |
| Liechtenstein | LIECHTENS |
| Lithuania | LITHUANIA |
| Luxembourg | LUXEMB |
| Macau | MACAU |
| Macedonia | MACEDONIA |
| Madagascar | MADAGASC |
| Malawi | MALAWI |
| Malaysia | MALAYSIA |
| Maldives | MALDIVES |
| Mali | MALI |
| Malta | MALTA |
| Marshall Islands | MARSHALL |
| Martinique | MARTINIQ |
| Mauritania | MAURITAN |
| Mauritius | MAURITIUS |
| Mayotte | MAYOTTE |
| Mexico | MEXICO |
| Moldova | MOLDOVA |
| Monaco | MONACO |
| Mongolia | MONGOLIA |
| Montserrat | MONTSERR |
| Morocco | MOROCCO |
| Mozambique | MOZAMBIQ |
| Multi-Country | MULTICTRY |
| Myanmar | MYANMAR |
| Namibia | NAMIBIA |
| Nauru | NAURU |
| Nepal | NEPAL |
| Netherlands | NETHERLND |
| Netherlands Antilles | NETHANTIL |
| New Caledonia | NEWCALED |
| New Zealand | NEWZEAL |
| Nicaragua | NICARAGUA |
| Niger | NIGER |
| Nigeria | NIGERIA |
| Niue | NIUE |
| Norfolk Island | NORFOLK |

Country codes (continued):

| Country | Code |
|---|---|
| North Korea | NORKOREA |
| Northern Mariana Islands | NORMARIAN |
| Norway | NORWAY |
| Oman | OMAN |
| Pakistan | PAKISTAN |
| Palau | PALAU |
| Panama | PANAMA |
| Papua New Guinea | PAPUANG |
| Paraguay | PARAGUAY |
| Peru | PERU |
| Philippines | PHILIPPIN |
| Poland | POLAND |
| Portugal | PORTUGAL |
| Puerto Rico | PUERTRIC |
| Qatar | QATAR |
| Reunion | REUNION |
| Romania | ROMANIA |
| Russia | RUSSIA |
| Rwanda | RWANDA |
| Saint Kitts And Nevis | STKITTS |
| Saint Lucia | STLUCIA |
| Saint Vincent And Grenadines | STVINCENT |
| Samoa | SAMOA |
| San Marino | SANMARINO |
| Sao Tome And Principe | SAOTOME |
| Saudi Arabia | SAUDARAB |
| Senegal | SENEGAL |
| Seychelles | SEYCHEL |
| Sierra Leone | SIERLEONE |
| Singapore | SINGAPORE |
| Slovakia | SLOVAKIA |
| Slovenia | SLOVENIA |
| Solomon Islands | SOLOMON |
| Somalia | SOMALIA |
| South Africa | SOUAFRICA |
| South Korea | SOUKOREA |
| Spain | SPAIN |
| Sri Lanka | SRILANKA |
| St. Helena | STHELENA |
| St. Pierre And Miquelon | STPIERRE |
| Suriname | SURINAME |
| Svalbard And Jan Mayen Islands | SVALBARD |
| Swaziland | SWAZILAND |
| Sweden | SWEDEN |
| Switzerland | SWITZ |
| Syria | SYRIA |
| Taiwan | TAIWAN |
| Tajikistan | TAJIK |
| Tanzania United Republic Of | TANZANIA |
| Thailand | THAILAND |
| Togo | TOGO |
| Tonga | TONGA |
| Trinidad And Tobago | TRINIDAD |
| Tunisia | TUNISIA |
| Turkey | TURKEY |
| Turkmenistan | TURKMEN |
| Turks And Caicos Islands | TURKCAICO |
| Tuvalu | TUVALU |
| Uganda | UGANDA |
| Ukraine | UKRAINE |
| United Arab Emirates | EMIRATES |
| United Kingdom | UNKINGDOM |
| United States | USA |
| Uruguay | URUGUAY |
| Uzbekistan | UZBEK |
| Vanuatu | VANUATU |
| Venezuela | VENEZUELA |
| Viet Nam | VIETNAM |
| Virgin Islands (british) | VIRGBRIT |
| Virgin Islands (u.s.) | VIRGUS |
| Wallis And Futuna Islands | WALLIS |
| Western Sahara | WESSAHARA |
| Yemen | YEMEN |
| Yugoslavia | YUGOSLAV |
| Zaire | ZAIRE |
| Zambia | ZAMBIA |

## ETF Family

#### `ETFFamily`
Returns the ETF's family code as a string. Applies to ETFs only; for ordinary stocks it returns no value.

#### `ETFFamilySet(x1[, x2..x30])`
Evaluates to true when the ETF's family matches any of the up to 30 codes passed as arguments. Applies to ETFs only.

Valid family codes (use these string values as the function arguments):

| Family | Code |
|---|---|
| BLDRS | BLDRS |
| Claymore | CLAYMORE |
| Closed End Funds | CEFS |
| Currency Shares (Rydex) | CURRENCY |
| Direxion | DIREXION |
| Exchange Traded Notes | ETNS |
| First Trust | FTRUST |
| FocusShares | FOCUS |
| HealthShares | HEALTHSH |
| HOLDRS | HOLDRS |
| iShares | ISHARES |
| Macro Shares | MACROSH |
| Market Vectors | MVECTORS |
| Miscellaneous | MISCL |
| NETS (Northern Trust) | NETS |
| PowerShares | POWERSH |
| ProShares | PROSH |
| Realty Funds | REALTY |
| RevenueShares | REVSH |
| Rydex | RYDEX |
| SPA | SPA |
| SPDR | SPDR |
| TDX Independence | TDX |
| United States Trust | USTRUST |
| Vanguard | VANGUARD |
| Wisdom Tree | WISDOM |

## ETF Method

#### `ETFMethod`
Returns the ETF's method code as a string. Applies to ETFs only; for ordinary stocks it returns no value.

#### `ETFMethodSet(x1[, x2..x30])`
Evaluates to true when the ETF's method matches any of the up to 30 codes passed as arguments. Applies to ETFs only.

Valid method codes (use these string values as the function arguments):

| Method | Code |
|---|---|
| Hedged | HEDGED |
| Leveraged Long | LEVLONG |
| Leveraged Short | LEVSHORT |
| Quant Model | QUANT |
| Special Weights | SPWEIGHTS |
| Standard Long | STANLONG |
| Standard Short | STANSHORT |

## ETF Region

#### `ETFRegion`
Returns the ETF's region code as a string. Applies to ETFs only; for ordinary stocks it returns no value.

#### `ETFRegionSet(x1[, x2..x30])`
Evaluates to true when the ETF's region matches any of the up to 30 codes passed as arguments. Applies to ETFs only.

Valid region codes (use these string values as the function arguments):

| Region | Code |
|---|---|
| Asia | ASIA |
| BRIC-Chindia | BRIC |
| Developed | DEVELOP |
| Emerging | EMERG |
| Europe | EUROPE |
| Global | GLOBAL |
| Global Ex US | GLOBALXUS |
| Latin America | LATIN |
| MidEast-Africa | MIDEAST |
| North America | NAMERICA |
| Pacific Ex Japan | PACIFIC |

## ETF Sector

#### `ETFSector`
Returns the ETF's sector code as a string. Applies to ETFs only; for ordinary stocks it returns no value.

#### `ETFSectorSet(x1[, x2..x30])`
Evaluates to true when the ETF's sector matches any of the up to 30 codes passed as arguments. Applies to ETFs only.

Valid sector codes (use these string values as the function arguments):

| Sector | Code |
|---|---|
| Agriculture | AGRIC |
| Alternate Energy | ALTENERGY |
| Consumer | CONSUMER |
| Energy | ENERGY |
| Financial | FINANCIAL |
| General | GENSECT |
| Healthcare | HEALTHCAR |
| Housing | HOUSING |
| Industrials | INDUST |
| Infrastructure | INFRASTR |
| Materials | MATERIALS |
| Municipal fixed inc | MUNIS |
| Precious Metals | PRECIOUS |
| Real Estate | REALEST |
| Resources (General) | RESOURC |
| Services | SERVICES |
| Social | SOCIAL |
| Special Theme | SPECIAL |
| Taxable Fixed Inc | TXFIXINC |
| Technology | TECHNOL |
| Telecomm | TELECOMM |
| Timber | TIMBER |
| Transportation | TRANSPORT |
| Utilities | UTILITIES |
| Water | WATER |

## ETF Size

#### `ETFSize`
Returns the ETF's size code as a string. Applies to ETFs only; for ordinary stocks it returns no value.

#### `ETFSizeSet(x1[, x2..x30])`
Evaluates to true when the ETF's size matches any of the up to 30 codes passed as arguments. Applies to ETFs only.

Valid size codes (use these string values as the function arguments):

| Size | Code |
|---|---|
| General | GENSIZE |
| Large-Mega | ETF_LARGECAP |
| Mid | ETF_MIDCAP |
| Small-Micro | ETF_SMALLCAP |

## ETF Style

#### `ETFStyle`
Returns the ETF's style code as a string. Applies to ETFs only; for ordinary stocks it returns no value.

#### `ETFStyleSet(x1[, x2..x30])`
Evaluates to true when the ETF's style matches any of the up to 30 codes passed as arguments. Applies to ETFs only.

Valid style codes (use these string values as the function arguments):

| Style | Code |
|---|---|
| Equity Income | EQINCOME |
| General | GENSTYLE |
| General Fixed Inc | GENFIXINC |
| Growth | GROWTH |
| High Yield Fixed Inc | HIGHYLD |
| Intermediate Fixed Inc | INTFIXINC |
| Long Fixed Inc | LTFIXINC |
| Short Fixed Inc | STFIXINC |
| Value | VALUE |

## Common Mistakes

| Wrong (do not use) | Correct | Note |
|---|---|---|
| `ETFAsset` | `ETFAssetClass` | The asset-class factor is `ETFAssetClass`; the membership function is `ETFAssetClassSet`. |
| `ETFCntry` | `ETFCountry` | The country factor name is spelled out: `ETFCountry` / `ETFCountrySet`. |
| `ETFSectorIn` | `ETFSectorSet` | Membership functions use the "Set" suffix (e.g. `ETFSectorSet`), not an "In" suffix. |

## See Also

- [industry-sector.md](industry-sector.md) - RBICS sector/industry classification for stocks.
- [misc.md](misc.md) - country IDs for the stock `Country(...)` function (a different vocabulary from ETF country codes).
- [fundamentals.md](fundamentals.md) - the `Country` and `ExchCountry` functions for ordinary equities.
