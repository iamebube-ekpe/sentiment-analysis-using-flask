var NavBr = Vue.component('shownav', {
    data: function() {
        return {}
    },
    template: `
    <div>
        <nav class="navbar navbar-dark bg-secondary">
            <div class="container-fluid">
                <a href="" class="navbar-brand">Navbar</a>
            </div>
        </nav>
    </div>
    `
});



var app = new Vue({
    el: '#app',
    components: {
        'shownav': NavBr
    }

});