function nav_toggle(sender){
    sender.classList.toggle('active')
}
function nav_selectAll(sender, event){
    event.preventDefault();
    event.stopPropagation();
    const details = sender.closest('details');
    const items = details.querySelectorAll('li a');
    for(const a of items){
        a.classList.add('active');
    }
}
function nav_deselectAll(sender, event){
    event.preventDefault();
    event.stopPropagation();
    const details = sender.closest('details');
    const items = details.querySelectorAll('li a');
    for(const a of items){
        a.classList.remove('active');
    }
}

document.addEventListener('htmx:load', function(sender){
    const references = document.querySelectorAll('omr');
    for(let ref of references){
        const manul_id = ref.closest('section').getAttribute("name");
        const ref_id   = ref.innerHTML;
        //以下这个判断只是因为htmx会多触发一次，临时解决
        if(ref_id.match(/^[0-9]+$/)){
            ref.setAttribute("hx-get", `/reference/manul/${manul_id}/${ref_id}`);
            ref.setAttribute("hx-trigger", "load");
            ref.setAttribute("hx-target", "this");
        }
    }
});

document.addEventListener('click', function(sender){
    const lang_options = document.querySelectorAll('header nav li.nav-dropdown details[open]');
    for(opt of lang_options){
        if (!opt.contains(sender.target)) {
            opt.removeAttribute('open');
        }
    }
});