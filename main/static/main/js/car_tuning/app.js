
function remove_detail(detail) {
    var audio = new Audio("/static/main/sounds/04715.mp3");
    audio.volume = 0.1; 
    audio.play();
    
    const component_seat = document.getElementById(detail + "_seat")
    const user_components = document.getElementById("user_components")

    if (component_seat.value) {

        const new_element = document.createElement("button")
        new_element.id = component_seat.value
        new_element.value = detail
        user_components.append(new_element)
        const new_element_image = document.createElement("img")
        new_element.append(new_element_image)
        
        const new_element_name = document.createElement("h1")
        new_element_name.innerText = component_seat.innerText
        new_element.setAttribute("class", component_seat.attributes.class.value.slice(-5))
        new_element.append(new_element_name)
        
        if (component_seat.value.includes("ecu")) {    
            new_element.setAttribute("onclick", "install_detail( 'ecu', '" + component_seat.value + "')")
            new_element_image.src = "/static/main/images/details/ecu.png"
        } else if (component_seat.value.includes("engine")) {
            new_element.setAttribute("onclick", "install_detail( 'engine', '" + component_seat.value + "')")
            new_element_image.src = "/static/main/images/details/engine.png"
        } else if (component_seat.value.includes("turbo")) {
            new_element.setAttribute("onclick", "install_detail( 'turbo', '" + component_seat.value + "')")
            new_element_image.src = "/static/main/images/details/turbo.png"
        } else if (component_seat.value.includes("clutch")) {
            new_element.setAttribute("onclick", "install_detail( 'clutch', '" + component_seat.value + "')")
            new_element_image.src = "/static/main/images/details/clutch.png"
        }
        
        component_seat.value = ""
        component_seat.querySelectorAll("img")[0].setAttribute("class", "car-box__span_tuning-box-element_no-selected")
        component_seat.querySelectorAll("h1")[0].setAttribute("class", "car-box__span_tuning-box-element_no-selected")
        component_seat.setAttribute("class", component_seat.attributes.class.value.slice(0, -5))
    }
}



function install_detail(detail, new_detail) {
    var audio = new Audio("/static/main/sounds/04715.mp3");
    audio.volume = 0.1; 
    audio.play();

    const component_seat = document.getElementById(detail + "_seat")
    const user_components = document.getElementById("user_components")
    const detail_new = document.getElementById(new_detail)
    
    if (component_seat.value) {

        const new_element = document.createElement("button")
        new_element.id = component_seat.value
        user_components.append(new_element)
        const new_element_image = document.createElement("img")
        new_element.append(new_element_image)
        
        const new_element_name = document.createElement("h1")
        new_element_name.innerText = component_seat.innerText
        new_element.setAttribute("class", component_seat.attributes.class.value.slice(-5))
        new_element.append(new_element_name)
        
        if (component_seat.value.includes("ecu")) {    
            new_element.setAttribute("onclick", "install_detail( 'ecu', '" + component_seat.value + "')")
            new_element_image.src = "/static/main/images/details/ecu.png"
        } else if (component_seat.value.includes("engine")) {
            new_element.setAttribute("onclick", "install_detail( 'engine', '" + component_seat.value + "')")
            new_element_image.src = "/static/main/images/details/engine.png"
        } else if (component_seat.value.includes("turbo")) {
            new_element.setAttribute("onclick", "install_detail( 'turbo', '" + component_seat.value + "')")
            new_element_image.src = "/static/main/images/details/turbo.png"
        } else if (component_seat.value.includes("clutch")) {
            new_element.setAttribute("onclick", "install_detail( 'clutch', '" + component_seat.value + "')")
            new_element_image.src = "/static/main/images/details/clutch.png"
        }

    } 

    component_seat.querySelectorAll(".car-box__span_tuning-box-element_no-selected").forEach(element => {
        element.removeAttribute("class");
    });

    component_seat.value = new_detail
    component_seat.setAttribute("onclick", "remove_detail('" + detail + "')")

    if (component_seat.attributes.class.value.includes("lvl-")) {
        
        component_seat.setAttribute("class", component_seat.attributes.class.value.slice(0, -5) + " " + detail_new.attributes.class.value)
    } else {
        component_seat.setAttribute("class", component_seat.attributes.class.value + " " + detail_new.attributes.class.value)
    }

    user_components.removeChild(detail_new)

    

    
}



