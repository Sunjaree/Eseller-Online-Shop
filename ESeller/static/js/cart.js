var updateBtns = document.getElementsByClassName('update-cart')

for(var i=0; i<updateBtns; i++){

    updateBtns[i].addEventListener('click', function(){

        var product_id = this.dataset.product
        var action = this.dataset.action
        console.log(product_id, action)

    })

}
