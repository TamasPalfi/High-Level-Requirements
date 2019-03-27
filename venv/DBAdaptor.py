class InvalidObjectTypeException(exception):
    pass


class DBAdaptor:
    def __init__(self, obj_type):
        self.obj_type = obj_type.lower()

    if self.type == 'member':

        def get_member(self, obj_id):
            # Return Member obj from DB
            pass

        def set_member(self, new_information: dict(), obj_id) -> bool:
            # Allow information about a member to be set in database
            # Takes dictionary as input - Keys should be what parameters need to be changed
            # Values are information being changed
            # Returns true if information change was successful
            # False otherwise
            pass

        def remove_member(self, obj_id) -> bool:
            # Returns true if member removal was successful
            # False otherwise
            pass

        # Not sure if we even needs these methods
        # If we return a Member object with get_member()
        # Then can't the model teams just use the data parameters associated with that member
        # And write these methods themselves?

        def get_name(self, obj_id) -> str:
            # return concatenation of first and last name
            pass

        def get_first_name(self, obj_id) -> str:
            # return first name
            pass

        def get_last_name(self, obj_id) -> str:
            # return last name
            pass

        def get_email(self, obj_id) -> str:
            # return email
            pass

        def get_pw(self, obj_id) -> str:
            # return password
            pass

        def get_cc_num(self, obj_id) -> str:
            # return credit card number
            pass

        def get_is_admin(self, obj_id) -> bool:
            # return is_admin
            pass

        def get_is_idol(self, obj_id) -> bool:
            # return is_idol
            pass

        def get_points(self, obj_id) -> int:
            # return current points amount
            pass

        def get_visibility(self, obj_id) -> bool:
            # return if the member has their visibility set to private or not
            # true = private, false = non-private
            pass

        def get_invited_by(self, obj_id):
            # return member id of the member that invited this particular member
            # null for both admin and idol
            # so check if get_is_admin or get_is_idol is true and return null if so
            pass

        def get_dob(self, obj_id):
            # return a member's date of birth
            pass

        def get_address(self, obj_id) -> str:
            # return a members current address
            pass

        def get_phone_number(self, obj_id) -> str:
            # return a members most recent phone number
            pass

    elif self.type == 'post':

        def get_post(self, obj_id):
            # Return Post obj from DB
            pass

        def set_post(self, new_information: dict(), obj_id) -> bool:
            # Allow information about an object to be set in database
            # Takes dictionary as input - Keys should be what parameters need to be changed
            # Values are information being changed
            # Returns true if information change was successful
            # False otherwise
            pass

        def remove_post(self, obj_id) -> bool:
            # Returns true if removal was successful
            # False otherwise
            pass

    elif self.type == 'comment':

        def get_comment(self, obj_id):
            # Return comment obj from DB
            pass

        def set_comment(self, new_information: dict(), obj_id) -> bool:
            # Allow information about an object to be set in database
            # Takes dictionary as input - Keys should be what parameters need to be changed
            # Values are information being changed
            # Returns true if information change was successful
            # False otherwise
            pass

        def remove_comment(self, obj_id) -> bool:
            # Returns true if removal was successful
            # False otherwise
            pass

    elif self.type == 'url':

        def get_url(self, obj_id):
            # Return URl obj from DB
            pass

        def set_url(self, new_information: dict(), obj_id) -> bool:
            # Allow information about an object to be set in database
            # Takes dictionary as input - Keys should be what parameters need to be changed
            # Values are information being changed
            # Returns true if information change was successful
            # False otherwise
            pass

        def remove_url(self, obj_id) -> bool:
            # Returns true if removal was successful
            # False otherwise
            pass

    elif self.type == 'shortened url':

        def get_shortened_url(self, obj_id):
            # Return shortened url obj from DB
            pass

        def set_shortened_url(self, new_information: dict(), obj_id) -> bool:
            # Allow information about an object to be set in database
            # Takes dictionary as input - Keys should be what parameters need to be changed
            # Values are information being changed
            # Returns true if information change was successful
            # False otherwise
            pass

        def remove_shortened_url(self, obj_id) -> bool:
            # Returns true if removal was successful
            # False otherwise
            pass

    elif self.type == 'image':

        def get_image(self, obj_id):
            # Return image obj from DB
            pass

        def set_image(self, new_information: dict(), obj_id) -> bool:
            # Allow information about an object to be set in database
            # Takes dictionary as input - Keys should be what parameters need to be changed
            # Values are information being changed
            # Returns true if information change was successful
            # False otherwise
            pass

        def remove_image(self, obj_id) -> bool:
            # Returns true if removal was successful
            # False otherwise
            pass

    elif self.type == 'filtered image':

        def get_filtered_image(self, obj_id):
            # Return filtered image obj from DB
            pass

        def set_filtered_image(self, new_information: dict(), obj_id) -> bool:
            # Allow information about an object to be set in database
            # Takes dictionary as input - Keys should be what parameters need to be changed
            # Values are information being changed
            # Returns true if information change was successful
            # False otherwise
            pass

        def remove_filtered_image(self, obj_id) -> bool:
            # Returns true if removal was successful
            # False otherwise
            pass

    # Not sure if I need the next few objects past this point
    elif self.type == 'filter':

        def get_filter(self, obj_id):
            # Return filter obj from DB
            pass

        def set_filter(self, new_information: dict(), obj_id) -> bool:
            # Allow information about an object to be set in database
            # Takes dictionary as input - Keys should be what parameters need to be changed
            # Values are information being changed
            # Returns true if information change was successful
            # False otherwise
            pass

        def remove_filter(self, obj_id) -> bool:
            # Returns true if removal was successful
            # False otherwise
            pass

    elif self.type == 'sponsored item':

        def get_sponsored_item(self, obj_id):
            # Return Post obj from DB
            pass

        def set_sponsored_item(self, new_information: dict(), obj_id) -> bool:
            # Allow information about an object to be set in database
            # Takes dictionary as input - Keys should be what parameters need to be changed
            # Values are information being changed
            # Returns true if information change was successful
            # False otherwise
            pass

        def remove_sponsored_item(self, obj_id) -> bool:
            # Returns true if removal was successful
            # False otherwise
            pass

    else:
        raise InvalidObjectTypeException('No Valid Object Type Passed In')
