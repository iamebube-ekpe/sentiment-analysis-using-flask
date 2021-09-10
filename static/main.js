var NavBr = Vue.component('shownav', {
    data: function () {
        return {}
    },
    template: `
    <div>
        <nav class="navbar navbar-dark bg-secondary">
            <div class="container-fluid">
                <a href="" class="navbar-brand">EVEL</a>
            </div>
        </nav>
    </div>
    `
});

var Form = Vue.component('display-form', {
    data: function () {
        return {
            form: {
                twtId: '',
                numOfTwts: 0
            }
        }
    },
    methods: {
        async submitForm() {
            if (this.form.twtId === '') {
                alert('Please enter a twitter id');
                return;
            }
            if (this.form.numOfTwts === 0) {
                alert('Please enter number of tweets');
                return;
            } else if (this.form.numOfTwts > 10) {
                alert(`Please enter a number less than ${this.form.numOfTwts}`);
                return;
            }
            await axios.post('http://localhost:5000/api/analyze', this.form)
                .then(response => {
                    console.log(response);
                    this.form.twtId = '';
                    this.form.numOfTwts = 0;
                })

        }
    },
    template: `<div class="container-fluid">
        <div class="row">
            <div class="col"></div>
            <div class="col-sm-6 card-body" style="width: 15rem;">
                <form id='twtForm' @submit.prevent='submitForm()'>
                    <!-- Name input -->
                    <div class="form-outline mb-4">
                        <input type="text" id="form5Example1" class="form-control" autocomplete='off' v-model='form.twtId'/>
                        <label class="form-label" for="form5Example1">ID/Name Of Twitter Account</label>
                    </div>

                    <!-- Email input -->
                    <div class="form-outline mb-4">
                        <input type="number" id="form5Example2" class="form-control" autocomplete='off' v-model='form.numOfTwts' />
                        <label class="form-label" for="form5Example2">Number Of Tweets to process (Maximum 10)</label>
                    </div>

                    <!-- Submit button -->
                    <button type="submit" class="btn btn-primary btn-block mb-4">Send</button>
                </form>
            </div>
            <div class="col"></div>
        </div>
    </div>
`
})



var app = new Vue({
    el: '#app',
    components: {
        'shownav': NavBr,
        'display-form': Form
    }

});