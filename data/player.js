var displayNames = function(data){

    $("#bottom").empty()
    $.each(data, function(i, player){

        var id = player["id"]
        var row = $("<div class='card mx-2 d-flex col-md-3 mb-4 px-4 '>" 
                    + "<img id=bttn_"+id+" class='card-img-top resizeView1' alt="+player["name"]+" src= '"+player["image"]+"'/>" 
                    + "<div class='card-body'>" + "<h4 class='card-title'>" + player["name"] + "</h4>" 
                    + "<h6 class='card-text'>" + player["country"] + "</h6>" + "</div>" + "</div>")
       
        $("#bottom").append(row)

        $("#bttn_"+id).click(function(){
            window.location.href = '/view/' + id; 
        })
            

    })
    var len = $('.card').length
    if (len == 0)
        $("#bottom_top").append("<div class='cont'> We've found " +"<strong>zero</strong>"+ " results </div>")
    else
        $("#bottom_top").append("<div class='cont'> We've found "+"<strong>" +len + "</strong>"+ " results... </div>")

}

var searchData = function(name){
       
    $.ajax({
        type: "POST",
        url: "/search",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(name),
        success: function(result){

            displayNames(result["players"])
            $("#search-field").val('')
            $("#search-field").focus()
            
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

var creatingNew = function(){
    $("#adding_new").empty()
    
    var row = $("<div class='divC'>"+"<h2 class=''> Create a new player </h2>")
    var name_create = $("<div >"+"<input class='design_input' type='text' id='name-input' placeholder='name...'>"+"</div>")
    var image_create = $("<div >"+"<input class= 'design_input' type='text' id='image-input' placeholder='image...'>"+"</div>")
    var sum_create = $("<div >"+"<input class= 'design_input' type='text' id='sum-input' placeholder='summary...'>"+"</div>")
    var year_create = $("<div >"+"<input class= 'design_input' type='number' id='year-input' placeholder='peak year...'>"+"</div>")
    var wc_create = $("<div >"+"<input class= 'design_input' type='number' id='wc-input' placeholder='world cup...'>"+"</div>")
    var country_create = $("<div >"+"<input class= 'design_input' type='text' id='country-input' placeholder='country...'>"+"</div>")
    var submitCreate = $("<button class='button' class='testt' id='button_create' type='button'>"+"Submit"+"</button>"+"</div>")

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
var edit_item = function(item_id,field,bool){
    var items = {"item_id":item_id,"field":field, "bool":bool};
    console.log(bool);
     $.ajax({
        type: "POST",
        url: "/delfield/"+item_id,                
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(items),
        cache: false,
        success: function(result){
            window.location.reload();
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        },
    })   
}
var edit_field= function(item_id,field){
     var items = {"item_id":item_id,"field":field, "val":$('#update_sum').text()};
     // console.log($('#update_sum').text())
     $.ajax({
        type: "POST",
        url: "/editfield/"+item_id,                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(items),
        cache : false,
        success: function(result){
            window.location.reload();

        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)

        },
    })   
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
            // console.log(players);
            id = players.length;
            // console.log(id);
            $("#bottom_create").append("<div class='text'>You have successfully added a new player to our list of the greatest soccer players ever<div>")
            $("#bottom_create").append("<div class='text1'>"+"<button id='button_view' type='button'>"+"view"+"</button>" +"</div>")
            $("#button_view").click(function(){ 
                // alert("hi")
                window.location.href = '/edit/' + id;  
            })
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        },
    })

    var name = $("#name-input").val()
    var image = $("#image-input").val()
    var summary = $("#sum-input").val()
    var peak_year = $("#year-input").val() 
    var world_cup = $("#wc-input").val()
    var country = $("#country-input").val()
    
    if (!$.trim(name).length){
        $("#name-input").focus()
        $("#name-input").addClass("red")
        $("#name-input").attr("placeholder", "Please enter a name")
        $("#name-input").after('<span class="check_name">required</span>').next('.check_client');
        $('.check_name').css('color', 'red');
    } if (!$.trim(image).length) {
        $("#image-input").focus()
        $("#name-input").addClass("clear")
        $("#image-input").addClass("red")
        $("#image-input").attr("placeholder", "Please enter an image")
        $("#image-input").after('<span class="check_image">required</span>').next('.check_client');
        $('.check_image').css('color', 'red');
    }
    if (!$.trim(summary).length) {
        $("#sum-input").focus()
        $("#name-input").addClass("clear")
        $("#image-input").addClass("clear")
        $("#sum-input").addClass("red")
        $("#sum-input").attr("placeholder", "Please enter an input")
        $("#sum-input").after('<span class="check_sum">required</span>').next('.check_client');
        $('.check_sum').css('color', 'red');
    }
    if (!$.trim(peak_year).length) {
        $("#year-input").focus()
        $("#name-input").addClass("clear")
        $("#image-input").addClass("clear")
        $("#sum-input").addClass("clear")
        $("#year-input").addClass("red")
        $("#year-input").attr("placeholder", "please enter an number")
        $("#year-input").after('<span class="check_year">required</span>').next('.check_client');
        $('.check_year').css('color', 'red');
    }
    if (!$.trim(world_cup).length) {
        $("#wc-input").focus()
        $("#name-input").addClass("clear")
        $("#image-input").addClass("clear")
        $("#sum-input").addClass("clear")
        $("#year-input").addClass("clear")
        $("#wc-input").addClass("red")
        $("#wc_input").attr("placeholder", "Please enter a number")
        $("#wc-input").after('<span class="check_wc">required</span>').next('.check_client');
        $('.check_wc').css('color', 'red');
    } 
    if (!$.trim(country).length) {
        $("#country-input").focus()
        $("#name-input").addClass("clear")
        $("#image-input").addClass("clear")
        $("#sum-input").addClass("clear")
        $("#year-input").addClass("clear")
        $("#wc-input").addClass("clear")
        $("#country-input").addClass("red")
        $("#country-input").attr("placeholder", "Please enter a country")
        $("#country-input").after('<span class="check_country">required</span>').next('.check_client');
        $('.check_country').css('color', 'red');
    } 

    if (!$.trim(name).length || !$.trim(image).length || !$.trim(summary).length || !$.trim(peak_year).length || !$.trim(country).length || !$.trim(world_cup).length) {
            $(document).find("#button_create").attr('disabled', true);
    }
}
$(document).ready(function(){
    // $(document).find("#search-field").focus()
    // $("#search-field").autocomplete({
    //   source: names
    // })
    $("#name-input").on("input", function(event){

            if (event.target.value){
                 $('.check_name').remove();

            }
    });
    $("#image-input").on("input", function(event){

            if (event.target.value){
                 $('.check_image').remove();

             }
    });
    $("#sum-input").on("input", function(event){ 

            if (event.target.value){
                 $('.check_sum').remove();

            }
    });
    $("#year-input").on("input", function(event){

            if (event.target.value){
                 $('.check_year').remove();

            }
    });
    $("#wc-input").on("input", function(event){

            if (event.target.value){
                $('.check_wc').remove();

            }
    });
    $("#country-input").on("input", function(event){

            if (event.target.value){
                 $('.check_country').remove();

            }
    });
    // displayNames(players);
     $("#add").click(function(){                
        var name = $("#search-field").val()
        // alert("hi");
        searchData(name)
    })

    //enter function
    $("#search-field").keypress(function (e) {
      if (e.which == 13) {
        // alert("hi");
         e.preventDefault();
         $("#add").click();
     }
   })

    //creating a new item

    $("#create").click(function(){ 
        $(document).find("#button_create").attr('disabled', true);
        // $('.testt').attr('disabled', true);
        creatingNew();

    })
    // edit when clicking on the item
    $(document).find('.bttn_save').hide()
    $(document).find('.bttn_cancel').hide()
    $(document).find('.bttn_undo').hide()

    //edit summary
    $(document).on('click', '.bttn_editable', function(event){
        
        event.preventDefault();
        var elment = $(this).attr('div');
        console.log($(this));
        var item_id = $('.item_to_edit').attr('item_id');
        // console.log (item_id)
        $(document).find('.bttn_save').show();
        $(document).find('.bttn_cancel').show();
        $(document).find('.bttn_editable').hide();
        $('.item_to_edit').attr('contenteditable', 'true');
        $('.item_to_edit').addClass('bg-warning').css('padding', '5px');
        $('.item_to_edit').focus();
        $('.item_to_edit').attr('original_entry', $(this).html());

    })
    $(document).on('click', '.bttn_save', function(event){
        $(document).find('.bttn_save').hide();
        $(document).find('.bttn_cancel').hide();
        $(document).find('.bttn_editable').show();
        event.preventDefault();
        // if ($(this).attr('edit_type') == 'button'){
        //     return false;
        // }
        var elment = $('.item_to_edit').closest('div');
        $('.item_to_edit').removeAttr('contenteditable');
        $('.item_to_edit').removeClass('bg-warning')
        $('.item_to_edit').css('padding', '');
        var arr = {elment};
        $.extend(arr, {elment});
        // $('.post_msg').html('<pre class="bg-success">'+JSON.stringify(arr, null, 2) + '</pre>');
    })

    $(document).on('click', '.bttn_cancel', function(event){
        $(document).find('.bttn_save').hide();
        $(document).find('.bttn_cancel').hide();
        $(document).find('.bttn_editable').show()
        event.preventDefault();
        // if ($(this).attr('edit_type') == 'button'){
        //     return false;
        // }
        var span_id = $('.item_to_edit');
        $('.item_to_edit').removeAttr('contenteditable');
        $('.item_to_edit').removeClass('bg-warning').css('padding', '');
        $('.item_to_edit').html($(this).attr('original_entry'));
        // $('.post_msg').html('<pre class="bg-success">'+JSON.stringify(arr, null, 2) + '</pre>');
    })
    var x ;
    $(document).on('click', '.bttn_del', function(event){

          $(document).find('.bttn_del').hide();
          $(document).find('.bttn_editable').hide();
          $(document).find('.bttn_undo').show();

     })

    $(document).on('click', '.bttn_undo', function(event){
          $(document).find('.bttn_del').show();
          $(document).find('.bttn_editable').show();
          $(document).find('.bttn_undo').hide();
          
          
    })

    // //contry edit
    // $(document).on('click', '.bttn_editable', function(event){
        
    //     event.preventDefault();
    //     var elment = $(this).attr('div');
    //     console.log($(this));
    //     var item_id = $('.item_to_edit_cnt').attr('item_id');
    //     // console.log (item_id)
    //     $(document).find('.bttn_save').show();
    //     $(document).find('.bttn_cancel').show();
    //     $(document).find('.bttn_editable').hide();
    //     $('.item_to_edit_cnt').attr('contenteditable', 'true');
    //     $('.item_to_edit_cnt').addClass('bg-warning').css('padding', '5px');
    //     $('.item_to_edit_cnt').focus();
    //     $('.item_to_edit_cnt').attr('original_entry', $(this).html());

    // })
    // $(document).on('click', '.bttn_save', function(event){
    //     $(document).find('.bttn_save').hide();
    //     $(document).find('.bttn_cancel').hide();
    //     $(document).find('.bttn_editable').show();
    //     event.preventDefault();
    //     // if ($(this).attr('edit_type') == 'button'){
    //     //     return false;
    //     // }
    //     var elment = $('.item_to_edit_cnt').closest('div');
    //     $('.item_to_edit_cnt').removeAttr('contenteditable');
    //     $('.item_to_edit_cnt').removeClass('bg-warning')
    //     $('.item_to_edit_cnt').css('padding', '');
    //     var arr = {elment};
    //     $.extend(arr, {elment});
    //     // $('.post_msg').html('<pre class="bg-success">'+JSON.stringify(arr, null, 2) + '</pre>');
    // })

    // $(document).on('click', '.bttn_cancel', function(event){
    //     $(document).find('.bttn_save').hide();
    //     $(document).find('.bttn_cancel').hide();
    //     $(document).find('.bttn_editable').show()
    //     event.preventDefault();
    //     // if ($(this).attr('edit_type') == 'button'){
    //     //     return false;
    //     // }
    //     var span_id = $('.item_to_edit_cnt');
    //     $('.item_to_edit_cnt').removeAttr('contenteditable');
    //     $('.item_to_edit_cnt').removeClass('bg-warning').css('padding', '');
    //     $('.item_to_edit_cnt').html($(this).attr('original_entry'));
    //     // $('.post_msg').html('<pre class="bg-success">'+JSON.stringify(arr, null, 2) + '</pre>');
    // })

})

