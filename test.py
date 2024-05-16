from bitrix24 import Bitrix24
import json
bx = Bitrix24('https://easybooking.bitrix24.ru/rest/31387/g1ourrvecn2pk1e8/')


# # Working comment
# bx.callMethod(
# 	"crm.timeline.comment.add",
# 	{
# 		'fields':
# 		{
# 			"ENTITY_ID": 238725,
# 			"ENTITY_TYPE": "deal",
# 			"COMMENT": "New comment was added"
# 		}
# 	})


result  = bx.callMethod('crm.deal.fields', {
    'id' : "238725"
})
for key in result.keys():
    field = result[key]
    # print(field['type'])
    if field['type'] == 'enumeration':
        if field['listLabel'] == 'Статус промокода':
            print(key)
            print(json.dumps(field, indent=4, ensure_ascii=False))

# bx.callMethod('crm.deal.update', {
#     'id' : '238725', 
#     'fields' : {
#         'UF_CRM_1715853973089' :  7141
#     }
# })


# bx.callMethod('crm.deal.userfield.update', {
#     'id' : "238725", 
#     'fields' : {
#             'UF_CRM_1715853973089' : 7143
#         }
#     }, 
# )