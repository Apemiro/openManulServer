# -*- coding: UTF-8 -*-

def __auto_lang(desc, lang):
    if type(desc)==str:
        return(desc)
    elif type(desc)==dict:
        if lang in desc:
            return(desc[lang])
        else:
            return(list(desc.values())[0])
    else:
        raise Exception(f"language format error: dict or str expected but {type(desc)} found")
        
def __lifetime(desc):
    if 'year_1' in desc:
        if 'year_2' in desc:
            return(f"{desc['year_1']} - {desc['year_2']}")
        else:
            return(f"{desc['year_1']} - ")
    else:
        if 'year_2' in desc:
            return(f"? - {desc['year_2']}")
        else:
            return(f"")

def fmt_card(indv, lang):
    htmx = f"""
    <section class="card">
        <div class="card-inner">
            <div class="card-face card-front">
                <img class="card-image" src="image/manul/{indv.get("ImgID","")}.png" alt="">
                <div class="card-overlay">
                    <h2 class="card-title">{__auto_lang(indv["name"], lang)}</h2>
                    <p class="card-description">{__lifetime(indv)}</p>
                </div>
            </div>
            <div class="card-face card-back">
                <h2 class="card-title">{__auto_lang(indv["name"], lang)}</h2>
                <p class="card-description">{__auto_lang(indv.get("info",{"_":""}), lang)}</p>
            </div>
        </div>
    </section>
    """
    return(htmx)
