# -*- coding: UTF-8 -*-
import json
import yaml

class OpenManulDataService:
    """OpenManul Data Service Class for OpenManulServer"""
    def __init__(self, path):
        self.manuls = {}
        
        filename = "/".join([path, "data", "individuals", "manul", "names.yaml"])
        with open(filename, encoding="utf8") as f:
            names = yaml.safe_load(f)
            for name in names:
                manul_id = name["ID"]
                if manul_id in self.manuls: raise Exception("repeated manul ID")
                self.manuls[manul_id] = name
        
        filename = "/".join([path, "data", "individuals", "manul", "information.yaml"])
        with open(filename, encoding="utf8") as f:
            infos = yaml.safe_load(f)
            for info in infos:
                manul_id = info["ID"]
                if manul_id not in self.manuls: raise Exception("manul ID not found")
                for k in info:
                    self.manuls[manul_id][k] = info[k]
        
        self.image_credits = {}
        
        filename = "/".join([path, "data", "individuals", "manul", "image_credit.yaml"])
        with open(filename, encoding="utf8") as f:
            images = yaml.safe_load(f)
            for img in images:
                image_id = img["ImgID"]
                if image_id in self.image_credits: raise Exception("repeated image ID")
                self.image_credits[image_id] = img
                manul_id = "_".join(image_id.split("_")[:-1])
                if manul_id in self.manuls:
                    if "ImgID" not in self.manuls[manul_id]:
                        self.manuls[manul_id]["ImgID"] = image_id
                else:
                    raise Exception("manul of image ID not found")

    def __del__(self):
        pass

    def getIndividuals(self, filter=""):
        return self.manuls


