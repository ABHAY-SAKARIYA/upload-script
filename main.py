import pandas as pd
import json
import math


class XlsxToJson:

    def __init__(self) -> None:
        self.XlsxData = pd.read_excel("New_Final_Data_xlsx_for_jyot_app/xlsx/youtube_posts_upload_data.xlsx")
        self.MainJsonData = []
        # print(self.XlsxData)


    @staticmethod
    def remove_nan(obj):
        if isinstance(obj, float) and math.isnan(obj):
            return None
        return obj

    @staticmethod
    def format_number(value):
        # Convert float to int if it's a whole number
        if isinstance(value, float) and value.is_integer():
            return int(value)
        return value

    def convertPost(self):

        for ind,value in self.XlsxData.iterrows():
            self.jsonData = {}

            for key in value.keys():
                if (pd.isna(value[key])):
                    continue
                
                if (key == "category_id" or key == "category_name"):
                    temp = value[key].split(",") 
                    self.jsonData[key] = temp
                else:
                    if(value[key] == " "):
                        self.jsonData[key] = "null"
                        continue
                    else:
                        self.jsonData[key] = self.format_number(value[key])

            self.MainJsonData.append(self.jsonData)

                


        # print(self.MainJsonData)
        with open("New_Final_Data_xlsx_for_jyot_app/json/YoutubeData.json","a", encoding="utf-8") as writefile:
            writefile.write(json.dumps(self.MainJsonData,indent=4,default=self.remove_nan))
        


    def convertCategory(self,fileName):
        categoryData = pd.read_excel(fileName);
        # print(categoryData.head());

        for ind,value in categoryData.iterrows():
            self.jsonData = {
            }

            for key in value.keys():
                if(pd.isna(value[key])):
                    continue
                if(key == "search_title" or key == "tag"):
                    if(type(value[key]) == float ):
                        continue
                    temp = value[key].split(",")
                    # print(temp);
                    self.jsonData[key] = temp
                else: 
                    if(value[key] == " "):
                        continue
                
                    self.jsonData[key] = self.format_number(value[key])
            self.MainJsonData.append(self.jsonData)

        print(self.MainJsonData);
        with open("New_Final_Data_xlsx_for_jyot_app/YoutubecategoryJsonData.json","a", encoding="utf-8") as writefile:
            writefile.write(json.dumps(self.MainJsonData,indent=4,default=self.remove_nan))
        

    def convertTags(self,fileName):
        tagsData = pd.read_excel(fileName);
        for ind,value in tagsData.iterrows():
            self.jsonData = {}

            for key in value.keys(): 
                if(pd.isna(value[key])):
                    continue
                if(value[key] == " "):
                    continue
            
                self.jsonData[key] = self.format_number(value[key])
            self.MainJsonData.append(self.jsonData)

        print(self.MainJsonData);
        with open("New_Final_Data_xlsx_for_jyot_app/TagsData.json","a", encoding="utf-8") as writefile:
                    writefile.write(json.dumps(self.MainJsonData,indent=4,default=self.remove_nan))



# converter = XlsxToJson()
# converter.convertPost()
# converter.convertCategory("New_Final_Data_xlsx_for_jyot_app/youtube_category_upload_sheet.xlsx")
# converter.convertTags("New_Final_Data_xlsx_for_jyot_app/podcasts_tags.xlsx");
