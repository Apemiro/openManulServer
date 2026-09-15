function omr_init(){
    document.addEventListener('DOMContentLoaded', () => {
        const elems = document.querySelectorAll('omr');
        for(elem of elems){
            elem.addEventListener('click', (event) => {
                /*
                if(check()){
                    window.location.assign("");
                }
                */
            });
        }
    });
}
