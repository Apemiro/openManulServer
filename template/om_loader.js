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

document.addEventListener('load', function(sender){
    const references = document.querySelectorAll('omr');
    for(ref of references){
        const manul_id = ref.closest('section').name;
        const ref_id   = ref.innerHtml;
        ref.hxGet      = `/references/manul/${manul_id}/${ref_id}`;
        ref.hxTrigger  = "load";
        ref.hxTarget   = "this";
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