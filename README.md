Let's make some cookies!

## Setup

1. Fork and clone [this repository](https://github.com/JoinCODED/TASK-Django-M10-Forms).
2. Install the `requirements` using `pip install -r requirements/dev.lock`.
3. Run the `migrations`.

## Task

### Create Form

1. Create a `forms.py` module inside the `stores` package.
2. Create a `form` called `StoreItemForm` for `StoreItem` with the following fields `name`, `description`, `kind`, and `price`.
3. Add a `view` for items and call it `create_store_item`. Create a new instance of `StoreItemForm` in your view and add it to your `context`, and `render` a template that you will create shortly, called `create_store_item.html`.
4. Add your `create_store_item` view to `urls.py` and name it `create-store-item`:
5. Add your template in `stores/templates/create_store_item.html`.
   - Render the form in the body
   - Add a `button` with `type="submit"`
6. Wrap your `form` variable in the template with a `form` HTML tag.
   - Add `action` to your `form` HTML tag equal to `{% url 'create-store-item' %}`
   - Add the `method` to your `form` HTML tag to be equal to `POST`
   - Add a `{% csrf_token %}` inside the `form` HTML tag, right before your `form` variable
7. Handle the `POST` request now inside your `view` when the form is submitted.
   - Check if the `request.method` is `POST`, and then create a new instance of `StoreItemForm` and pass `request.POST` as the first argument
   - Check if the `form` is valid, then save the form if it is and redirect to `store-item-list`
