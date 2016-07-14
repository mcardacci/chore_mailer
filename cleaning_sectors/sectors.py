class Sector():
    def one(self):
        return """
        <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">          
                <meta name="viewport" content="width=device-width,initial-scale=1">
                <title>Chore List</title>
                <link rel="stylesheet" href="stylesheet.css" type="text/css">
            </head>
            <body>
                <fieldset>
                    <legend>
                        Have you done your Chores this Week?
                    </legend>
                    <input type="checkbox" class="list-item"/>Sweep Floor including Laundry Room<br/>
                    <input type="checkbox" class="list-item"/>Swiffer Floor including Laundry Room<br/>
                    <input type="checkbox" class="list-item"/>Wipe down faucet<br/>
                    <input type="checkbox" class="list-item"/>Wipe down counter top<br/>
                    <input type="checkbox" class="list-item"/>Wipe down sink<br/>
                    <input type="checkbox" class="list-item"/>If trash cans are stinky: spray with cleaner, let dry, wipe down with moist towel<br/>
                    <input type="checkbox" class="list-item"/>Wipe down refrigerator<br/>
                    <input type="checkbox" class="list-item"/>Wipe down stove top and stove door<br/>
                </fieldset>
                <!--<script src="strikethrough.js"></script>-->
            </body>
        </html>
        """
    def two(self):
        return """
        <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">          
                <meta name="viewport" content="width=device-width,initial-scale=1">
                <title>Chore List</title>
                <link rel="stylesheet" href="stylesheet.css" type="text/css">
            </head>
            <body>
                <fieldset>
                    <legend>
                        Have you done your Chores this Week?
                    </legend>
                    <input type="checkbox" class="list-item"/>Wipe down faucet<br/>
                    <input type="checkbox" class="list-item"/>Wipe down sink<br/>
                    <input type="checkbox" class="list-item"/>Wipe down metal housing of glass doors<br/>
                    <input type="checkbox" class="list-item"/>Windex Mirror<br/>
                    <input type="checkbox" class="list-item"/>Windex glass doors<br/>
                    <input type="checkbox" class="list-item"/>Wipe down toilet with cleaner<br/>
                    <input type="checkbox" class="list-item"/>Scrub inside of toilet with brush<br/>
                    <input type="checkbox" class="list-item"/>Wash bath rug if necessary<br/>
                    <input type="checkbox" class="list-item"/>Spray and scrub bath tub<br/>
                    <input type="checkbox" class="list-item"/>Spray and scrub faucet<br/>
                    <input type="checkbox" class="list-item"/>Spray and scrub tiles<br/>
                    <input type="checkbox" class="list-item"/>Spray and scrub shower head<br/>
                </fieldset>
                <!--<script src="strikethrough.js"></script>-->
            </body>
        </html>
        """

    def three(self):
        return """
        <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">          
                <meta name="viewport" content="width=device-width,initial-scale=1">
                <title>Chore List</title>
                <link rel="stylesheet" href="stylesheet.css" type="text/css">
            </head>
            <body>
                <fieldset>
                    <legend>
                        Have you done your Chores this Week?
                    </legend>
                    <input type="checkbox" class="list-item"/>Dust Furniture, Crevices and wherever necessary<br/>
                    <input type="checkbox" class="list-item"/>Water Plants<br/>
                    <input type="checkbox" class="list-item"/>Sweep Floor<br/>
                    <input type="checkbox" class="list-item"/>Swiffer Floor<br/>
                </fieldset>
                <!--<script src="strikethrough.js"></script>-->
            </body>
        </html>
        """
# ----------------------------- TESTING ---------------------------------
# sec = Sector()
# print sec.one()
# print sec.two()
# print sec.three()
