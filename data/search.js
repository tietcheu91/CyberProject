
var displayNames = function(data){
    //empty old data
    $("#bottom").empty()
    //insert all new data
    $.each(data, function(i, player){
        // var new_player = $("<div class='row'>"+"<div class="" 'col-md-3'>" + player["name"] + "<img src= '"+player["image"]+"'/>"+ "</div>" + "</div>"+
        //           "<div class= 'col-md-3'>" + player["country"] + "</div>")
        var id = player["id"]
        // console.log(id)
        var row = $("<div class='row'>"+"<div class='col-md-2 cont' id='name_"+id+"'>" + player["name"] + "</div>" + 
                    "<div class='col-md-2'>"+ "<button class='button' id=bttn_"+id+">"+"Details"+"</button>"+ "</div>"+
                    "<div class='col-md-2'>"+ "<button class='button' id=del_"+id+">"+"X"+"</button>"+"</div>"+"</div>")
        // var new_player = $("<div class='row'>"+"<div class="" 'col-md-3'>" + player["name"] + "<img src= '"+player["image"]+"'/>"+ "</div>" + "</div>"+
        //           "<div class= 'col-md-3'>" + player["country"] + "</div>")

        $("#bottom").append(row)
        // var new_player = $("<div  >"+ player["name"] + "</div>")
        // var submitid = $("<button class='button'>" + "more information" + "</button>")
        // var deleteid = $("<button class='button'>" + "X" + "</button>")
       
        // $().on(function(click, "#btt_"+id){ 
        //     // $("#bottom").empty()
        //     window.location.href = '/view/' + id; 

        // }) 

        $("#bttn_"+id).click(function(){
            // alert("details: "+id)
            window.location.href = '/view/' + id; 
        })


        

       
       


        $("#del_"+id).click(function(){
          $("#bottom").html("");
          // console.log("hhi");
          var data_to_save = {"id": player["id"]} 
          $.ajax({
            type: "POST",
            url: "del_data",                
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify(data_to_save),
            
            success: function(result){
              // sales = result.sales;
              displayNames(result["players"]);
              // console.log(sales);
          },
            error: function(request, status, error){
              console.log("Error");
              console.log(request)
              console.log(status)
              console.log(error)
          }

          });
        })
        
        
      
        // $("#bottom").append(new_player) 
        // $("#bottom").append(submitid)
        // $("#bottom").append(deleteid)

    })



}

var creatingNew = function(){
    //empty old data
    // $("#bottom_create").empty()
    // var row = $("<div class='row'>"+"<div class= 'col-md-1'>"+"<input type='text' id='id-input' placeholder='id...'>"+"</div>" +
    //               "<div class= 'col-md-1'>"+"<input type='text' id='name-input' placeholder='name...'>"+"</div>" +
    //               "<div class= 'col-md-1'>"+"<input type='text' id='image-input' placeholder='image...'>"+"</div>" +
    //               "<div class= 'col-md-1'>"+"<input type='text' id='sum-input' placeholder='summary...'>"+"</div>" +
    //               "<div class= 'col-md-1'>"+"<input type='text' id='year-input' placeholder='peak year...'>"+"</div>" +
    //               "<div class= 'col-md-1'>"+"<input type='text' id='wc-input' placeholder='world cup...'>"+"</div>" +
    //               "<div class= 'col-md-1'>"+"<input type='text' id='country-input' placeholder='country...'>"+"</div>" +
    //               "<button class=bttn_create id='button_create'>"+"Submit"+"</button>"+"</div>")

    // var id = $("#id-input").val()
    

    // console.log(id_create);
    var row = $("<div class='row'>")
    // var id_create= $("<div class= 'col-md-1'>"+"<input type='number' id='id-input' placeholder='id...'>"+"</div>")
    var name_create = $("<div class= 'col-md-1'>"+"<input type='text' id='name-input' placeholder='name...'>"+"</div>")
    var image_create = $("<div class= 'col-md-1'>"+"<input type='text' id='image-input' placeholder='image...'>"+"</div>")
    var sum_create = $("<div class= 'col-md-1'>"+"<input type='text' id='sum-input' placeholder='summary...'>"+"</div>")
    var year_create = $("<div class= 'col-md-1'>"+"<input type='number' id='year-input' placeholder='peak year...'>"+"</div>")
    var wc_create = $("<div class= 'col-md-1'>"+"<input type='number' id='wc-input' placeholder='world cup...'>"+"</div>")
    var country_create = $("<div class= 'col-md-1'>"+"<input type='text' id='country-input' placeholder='country...'>"+"</div>")
    var submitCreate = $("<button class='button enable' id='button_create' type='button'>"+"Submit"+"</button>"+"</div>")

    $(submitCreate).click(function(){ 
        create_item();
    })
    $("#bottom_create").append(row)
    $("#bottom_create").append(name_create)
    $("#bottom_create").append(image_create)
    $("#bottom_create").append(sum_create)
    $("#bottom_create").append(year_create)
    $("#bottom_create").append(wc_create)
    $("#bottom_create").append(country_create)
    $("#bottom_create").append(submitCreate)

}

var searchData = function(name){
    // var data_to_save = {"name": $("#search-field").val()}   
    // console.log(data_to_save)     
    $.ajax({
        type: "POST",
        url: "/search",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(name),
        //console.log(data)
        success: function(result){

            displayNames(result["players"])
            $("#search-field").val('')
            $("#search-field").focus()
            // console.log("comeon")
            
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

var create_item = function(){  
    var items = {"name": $("#name-input").val(), "image": $("#image-input").val(), "summary": $("#sum-input").val(), "peak_year": $("#year-input").val(), "world_cup": $("#wc-input").val(), "country": $("#country-input").val()}
    $.ajax({
        type: "POST",
        url: "/create",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(items),
        success: function(result){
            // console.log(all_data);
            var all_data = result["data"]

            id = result["id"]
            $("#bottom_create").append("<div>You have successfully added a new player to our list of the greatest soccer players ever<div>")
            $("#bottom_create").append("<a href = 'http://127.0.0.1:5000/view/31'>link </a>")

        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        },
    });
 // if (!$.trim($('#name-input').val()) || !$.trim($('#image-input').val()) || !$.trim($('#sum-input').val()) || !$.trim($('#year-input').val()) || !$.trim($('#wc-input').val()) || !$.trim($('#country-input').val()))
            // $("#button_submit").attr('disabled', 'disabled');
        // else 
            // console.log("here")
            // console.log(players["name"]);
            // $("#").attr('disabled', false);
    var name = $.trim($("#name-input").val())
    var image = $.trim($("#image-input").val())
    var summary = $.trim($("#sum-input").val())
    var peak_year = $.trim($("#year-input").val()) 
    var world_cup = $.trim($("#wc-input").val())
    var country = $.trim($("#country-input").val())

    if (name.length == 0 && !$('.check_client').length)
        $("#bottom_create").after('<span class="check_client">required</span>').next('.check_client');
        $('.check_client').css('color', 'red');
        
        $(name).focus()

    if (image.length == 0 && !$('.check_client').length)
        $("#bottom_create").after('<span class="check_client">required</span>').next('.check_client');
        $('.check_client').css('color', 'red');
        $(image).focus()

    if (summary.length == 0 && !$('.check_client').length)
        $("#bottom_create").after('<span class="check_client">required</span>').next('.check_client');
        $('.check_client').css('color', 'red');
        $(summary).focus()

    if (peak_year.length == 0 && !$('.check_client').length)
        $("#bottom_create").after('<span class="check_client">required</span>').next('.check_client');
        $('.check_client').css('color', 'red');
        $(peak_year).focus()

    if (world_cup.length == 0 && !$('.check_client').length)
        $("#bottom_create").after('<span class="check_client">required</span>').next('.check_client');
        $('.check_client').css('color', 'red');
        $(world_cup).focus()

    if (country.length == 0 && !$('.check_client').length)
        $("#bottom_create").after('<span class="check_client">required</span>').next('.check_client');
        $('.check_client').css('color', 'red');
        $(country).focus()
}

$(document).ready(function(){
    $('.enable').prop('disabled', true);
    $("#button_cancel").click(function(){ 
            window.location.href = '/view/' + id;  
        })
     
    $("#name-input").on("input", function(event){

            if (event.target.value){
                 $('.check_client').remove();

            }
    });
    $("#image-input").on("input", function(event){

            if (event.target.value){
                 $('.check_client').remove();

             }
    });
    $("#sum-input").on("input", function(event){ 

            if (event.target.value){
                 $('.check_client').remove();

            }
    });
    $("#year-input").on("input", function(event){

            if (event.target.value){
                 $('.check_client').remove();

            }
    });
    $("#wc-input").on("input", function(event){

            if (event.target.value){
                $('.check_client').remove();

            }
    });
    $("#country-input").on("input", function(event){

            if (event.target.value){
                 $('.check_client').remove();

            }
    });
                         
    $("#add").click(function(){                
        var name = $("#search-field").val()
        // console.log("hi");
        searchData(name)
    })

    $("#search-field").keypress(function (e) {
      if (e.which == 13) {
         e.preventDefault();
         $("#add").click();
     }
   })
     
     $("#button_edit").click(function(){ 
            // console.log(players);

            window.location.href = '/edit/' + id;  
        })

    // displayNames(players);
    $("#create").click(function(){   
        // console.log("click me");             
        creatingNew();
        // console.log("hi");
    })

    $("#button_submit").click(function(){
            players["name"] == ($.trim($("#edit-field").val())); 
            window.location.href = '/view/' + id; 
        })

})

// questions for the teacher 
// how to generate a global id
// Why is my link doesn't work
// do we need to have an edit button on all profile of name
// I am unable to replace the user input with the actual one 
// I am unable to return no results
// how do I get the error message when the created item doesn't match
