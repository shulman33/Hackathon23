import json

# JSON data as a string
s_json = '''
[{
    "CA_OwnerID": "FR_ACPR",
    "EntityCode": "PSD_PI!FR_ACPR!1376!50208",
    "EntityType": "PSD_AG",
    "Properties": [
        {"ENT_NAT_REF_COD": "440441681"},
        {"ENT_NAM": "M. JOSEPH Ebert"},
        {"ENT_ADD": "1 rue Bagasse"},
        {"ENT_TOW_CIT_RES": "MATOURY"},
        {"ENT_POS_COD": "97351"},
        {"ENT_COU_RES": "FR"},
        {"ENT_TYP_PAR_ENT": "PSD_PI"},
        {"ENT_COD_PAR_ENT": "FR_ACPR!1376"},
        {"DER_CHI_ENT_AUT": "Active"}
    ],
    "__EBA_EntityVersion": "20220428213506543"
},
{
    "CA_OwnerID": "FR_ACPR",
    "EntityCode": "PSD_PI!FR_ACPR!1376!49932",
    "EntityType": "PSD_AG",
    "Properties": [
        {"ENT_NAT_REF_COD": "453299471"},
        {"ENT_NAM": "Mme GUANNEL Marlène"},
        {"ENT_ADD": "Rue de l'Impératrice"},
        {"ENT_TOW_CIT_RES": "ST PIERRE"},
        {"ENT_POS_COD": "97250"},
        {"ENT_COU_RES": "FR"},
        {"ENT_TYP_PAR_ENT": "PSD_PI"},
        {"ENT_COD_PAR_ENT": "FR_ACPR!1376"},
        {"DER_CHI_ENT_AUT": "Active"}
    ],
    "__EBA_EntityVersion": "20220428213506543"
}]
'''

try:
    o_json = json.loads(s_json)
    filtered_data = [obj for obj in o_json if obj.get('EntityType', '') == 'PSD_AG']
    print(filtered_data)
    print(len(filtered_data))

except Exception as ex:
    print(repr(ex))
