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
    if "name" not in indv: raise Exception(f"manul ID: {indv["ID"]} has no name.")
    htmx = f"""
    <section class="card">
		<a class="bm" name="{indv["ID"]}">
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
		</a>
    </section>
    """
    return(htmx)

def fmt_zoo_filter(zoos, lang):
    li_list = []
    for zoo in zoos:
        li_list.append(f"""
                    <li><a href="javascript:void(0)" name="{zoo["ID"]}" onclick="nav_toggle(this)">{__auto_lang(zoo["name"], lang)}</a></li>
        """)
    li_list_dom = "".join(li_list)
    title = u"动物园列表"
    htmx = f"""
    <details class="nav-group" open>
        <summary>
            <h2>{title}</h2>
            <span class="summary-actions">
                <button type="button" class="summary-btn" title="Select all" onclick="nav_selectAll(this, event)"><i class="fa fa-check-square-o"></i></button>
                <button type="button" class="summary-btn" title="Deselect all" onclick="nav_deselectAll(this, event)"><i class="fa fa-square-o"></i></button>
                <i class="fa fa-chevron-down toggle-icon"></i>
            </span>
        </summary>
        <div class="collapsible-wrapper">
            <ul>
                {li_list_dom}
            </ul>
        </div>
    </details>
    """
    return(htmx)
