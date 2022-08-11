class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            # no prereq requirements for any courses
            return True
        
        # build adjacency list for both directions
        prereq_to_next = [None] * numCourses
        next_to_prereq = [None] * numCourses

        for prereq in prerequisites:
            next_c, prereq_c = prereq[0], prereq[1]
            
            if not prereq_to_next[prereq_c]:
                prereq_to_next[prereq_c] = set()
            if not next_to_prereq[next_c]:
                next_to_prereq[next_c] = set()
            
            prereq_to_next[prereq_c].add(next_c)
            next_to_prereq[next_c].add(prereq_c)

        q = deque()
        for course in range(numCourses):
            if not next_to_prereq[course]:
                # no prereqs needed to take this course
                q.append(course)
        if not q:
            # no courses with zero prereq
            # we cannot finish all courses
            return False
        
        completed_courses = [False] * numCourses
        while q:
            n = len(q)
            for i in range(n):
                course = q.popleft()
                if completed_courses[course]:
                    # we've taken this course
                    # before, loop detected
                    return False
                
                completed_courses[course] = True
                
                if prereq_to_next[course]:
                    # by taking this course, it might
                    # let us take next courses
                    for next_course in prereq_to_next[course]:
                        if next_to_prereq[next_course]:
                            # remove the prereq requirement for
                            # the next course
                            next_to_prereq[next_course].remove(course)
                            if len(next_to_prereq[next_course]) == 0:
                                # we've met all prereq requirements
                                # take this course!
                                q.append(next_course)
                                next_to_prereq[next_course] = None
        
        # check if we've taken all courses
        return all(completed_courses)               
