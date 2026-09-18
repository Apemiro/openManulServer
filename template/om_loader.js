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