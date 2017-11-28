'use strict';

function showMenu() {
    let btn = document.getElementById('menu-btn');
    let menu = document.getElementById('menu-block');
    let itemList = menu.querySelectorAll('.menu__item');

    btn.addEventListener('click', function() {
        for(let i=0; i < itemList.length; i++) {
            setTimeout(function(){
                itemList[i].classList.add('active');
            }, i * 300);
        }
    })

}


let SendComment = function () {
    this.chat = document.querySelector('.chat');
    this.form = document.querySelector('.d-comment');
    this.customText = this.form.querySelector('.comment__textarea');
    this.count = false;

    this.submitComment = function () {
        let _this = this;
        let submitBtn = this.form.querySelector('.d-comment__btn');

        submitBtn.addEventListener('click', function () {
            let textSend = _this.customText.innerHTML;
            let blockSend = document.createElement('textarea');

            blockSend.classList.add('visibility-hidden');

            blockSend.value = textSend;
            _this.form.appendChild(blockSend);
            // console.log(textSend);

            _this.getMessage(blockSend);

            if (_this.count) {
                _this.count = false;
            }
            else {
                _this.count = true;
            }

            blockSend.remove();
            document.querySelector('.comment__textarea').innerText = '';
        })
    };

    this.showMySmile = function() {
        let smileBtn = this.form.querySelector('.comment__smile-btn');

        smileBtn.addEventListener('click', function(){
            if(this.parentNode.classList.contains('comment__smile--active')) {
                this.parentNode.classList.remove('comment__smile--active');
            }
            else {
                this.parentNode.classList.add('comment__smile--active');
            }
        });
    };

    this.addSmile = function() {
       let smile = this.form.querySelectorAll('.smile-block__item');
       let _this = this;
       for( let item of smile) {
           item.addEventListener('click', function() {
               let smileImg = this.querySelector('.smile-block__img');
               _this.customText.appendChild(smileImg.cloneNode(true));
           })
       }

    };

    this.getMessage = function (content) {
        let textMessage = content.value;

        let messageBlock = document.createElement('div');
        messageBlock.classList.add('chat__block');
        if (this.count) {
            messageBlock.classList.add('chat__block--odd');
        }

        let messageSpan = document.createElement('span');
        messageSpan.classList.add('chat__comment');

        messageSpan.innerHTML = textMessage;
        messageBlock.appendChild(messageSpan);

        this.chat.appendChild(messageBlock);
    };

    this.init = function () {
        this.showMySmile();
        this.addSmile();
        this.submitComment();
    };
};


(function () {
    showMenu();
    let comment = new SendComment();
    comment.init();
}());