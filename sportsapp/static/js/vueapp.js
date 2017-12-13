var app = new Vue({
  el: '#app',
  data: {
    suggestions: []
  },
  mounted() {
    this.loadData();

    setInterval(function () {
      this.loadData();
    }.bind(this), 5000);
  },
  methods: {
    loadData: function () {
      console.log("Hello");
      $.get('suggestions/', function (response) {
        this.suggestions = response.suggestions;
        console.log(response);
      }.bind(this));
    }
  }
});
