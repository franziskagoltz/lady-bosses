import React, { Component } from 'react';


class CategorySelect extends Component {

    render() {
        return (
          <div>
            <h2> What are you looking for today? </h2>
            <form> 
              <div className="checkbox">
                <label>
                  <input type="checkbox" value="bakery" />
                  Bakery
                </label><br />
                <label>
                  <input type="checkbox" value="restaurant" />
                  Restaurant
                </label><br />
                <label>
                  <input type="checkbox" value="coffee & tea" />
                  Coffee & Tea
                </label><br />
                <label>
                  <input type="checkbox" value="desserts" />
                  Desserts
                </label>
              </div>
            </form>
          </div>
            )
    }

}

export default CategorySelect;