def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments
        Creates that number of users and a randomly distributed friendships
        between those users.
        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users

        # Create friendships
        # generate all possible friendship combinations

        # avoid dupes by ensuring the first number is smaller than the second

        # shuffle the possible friendships

        # create friendships for the first X pairs of the list
        # X determined by the formula num users * avg friendships // 2
        # need to divide by 2 since each add friendship creates 2 friendships