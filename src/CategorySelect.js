import React, { Component } from 'react';


class CategorySelect extends Component {

  render() {

    const options = ["bakery", "restaurant", "coffee & tea", "desserts", "bars",
                     "brewery", "pizza"];
    const inputs = options.map((option, index) => {
                    return (<label>
                            <input type="checkbox" key={index} value={option}/>
                            {option} <br />
                            </label>)
                  });

      return (

        <div>
          <h2> What are you looking for today? </h2>
          <form> 
            <div className="checkboxes">
              {inputs}
            </div>
          </form>
        </div>
          )
    }

}

export default CategorySelect;